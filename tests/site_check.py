import json
from pathlib import Path
from playwright.sync_api import sync_playwright

site = Path('index.html').resolve().as_uri()
session_site = Path('session.html').resolve().as_uri()
manifest = json.loads(Path('config/content-manifest.json').read_text(encoding='utf-8'))
certifications = manifest['certifications']
learning_paths = json.loads(Path('config/learning-paths.json').read_text(encoding='utf-8'))['paths']
sre_track = next(path for path in learning_paths if path['slug'] == 'sre-track')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto(site)
    page.wait_for_load_state('networkidle')
    cards = page.locator('.question-card')
    assert cards.count() == page.evaluate("window.questions.length")
    assert all(href.endswith('.html') for href in cards.locator('a').evaluate_all('(links) => links.map((link) => link.getAttribute("href"))'))
    page.locator('#search').fill('DNS')
    assert cards.count() > 0
    page.locator('#search').fill('')
    page.get_by_role('button', name='security').click()
    assert cards.count() > 0
    page.get_by_role('button', name='must-know study set').click()
    must_know_count = page.evaluate("window.questions.filter((question) => question.tags.includes('must-know')).length")
    assert cards.count() == must_know_count and page.url.endswith('#collection=must-know')

    # Certification tracks are manifest-derived, keyboard-accessible filters that
    # use URL hash state without creating duplicate Question themes.
    certificate_buttons = page.locator('#certification-filters button[data-certificate]')
    assert certificate_buttons.count() == len(certifications)
    assert certificate_buttons.evaluate_all('(buttons) => buttons.map((button) => button.dataset.certificate)') == [
        certification['tag'] for certification in certifications
    ]
    cka_count = page.evaluate("window.questions.filter((question) => question.tags.includes('cka')).length")
    page.get_by_role('button', name='CKA', exact=True).click()
    assert page.url.endswith('#certificate=cka')
    assert cards.count() == cka_count
    assert page.locator('#certification-filters button[data-certificate="cka"]').get_attribute('aria-pressed') == 'true'

    # A learning path is ordered data: the landing view offers it, and the view
    # renders a numbered sequence in manifest order instead of a filtered grid.
    assert page.locator('#path-entry').get_attribute('href') == '#path=sre-track'
    path_buttons = page.locator('#path-filters button[data-path]')
    assert path_buttons.evaluate_all('(buttons) => buttons.map((button) => button.dataset.path)') == [
        path['slug'] for path in learning_paths
    ]
    page.get_by_role('button', name=sre_track['title']).click()
    assert page.url.endswith('#path=sre-track')
    assert page.locator('#question-zone').is_hidden() and page.locator('#path-view').is_visible()
    steps = page.locator('#path-view .path-step')
    assert steps.count() == len(sre_track['steps'])
    assert steps.locator('.step-why').all_inner_texts() == [step['why'] for step in sre_track['steps']]
    assert steps.locator('.step-index').first.inner_text() == '01'
    expected_links = [step['question'].replace('.md', '.html') for step in sre_track['steps']]
    assert steps.locator('h3 a').evaluate_all(
        '(links) => links.map((link) => link.getAttribute("href"))'
    ) == expected_links
    assert all(why.strip() for why in steps.locator('.step-why').all_inner_texts())
    page.get_by_role('link', name='Back to the full database').click()
    # Leaving the path is hash-driven, so wait for the hashchange render rather
    # than reading the DOM in the same tick as the click.
    page.wait_for_function("() => document.querySelector('#path-view').hidden")
    assert page.locator('#question-zone').is_visible()

    # Hash navigation also works at a narrow touch viewport.
    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile.goto(f'{site}#certificate=lfcs')
    mobile.wait_for_load_state('networkidle')
    lfcs_count = mobile.evaluate("window.questions.filter((question) => question.tags.includes('lfcs')).length")
    assert mobile.locator('.question-card').count() == lfcs_count
    assert mobile.locator('#certification-filters button[data-certificate="lfcs"]').get_attribute('aria-pressed') == 'true'
    mobile.goto(f'{site}#collection=must-know')
    mobile.wait_for_load_state('networkidle')
    assert mobile.locator('.question-card').count() == mobile.evaluate("window.questions.filter((question) => question.tags.includes('must-know')).length")

    # The ordered path view is reachable by direct URL state at 390px, keeps its
    # sequence, and does not force the page to scroll sideways.
    mobile.goto(f'{site}#path=sre-track')
    mobile.wait_for_load_state('networkidle')
    mobile_steps = mobile.locator('#path-view .path-step')
    assert mobile_steps.count() == len(sre_track['steps'])
    assert mobile.locator('#question-zone').is_hidden()
    assert mobile_steps.locator('.step-index').all_inner_texts() == [
        f'{index:02d}' for index in range(1, len(sre_track['steps']) + 1)
    ]
    assert mobile.evaluate('document.documentElement.scrollWidth <= document.documentElement.clientWidth')

    # A narrow touch viewport can create, navigate, reveal, and share a session
    # without embedding a duplicate answer in browser data.
    mobile.goto(session_site)
    mobile.wait_for_load_state('networkidle')
    mobile.locator('#session-themes input[value="linux"]').check()
    mobile.locator('#session-themes input[value="kubernetes"]').check()
    mobile.locator('#session-total').fill('6')
    mobile.locator('#session-total').press('Tab')
    mobile.get_by_label('linux allocation').fill('3')
    mobile.get_by_label('kubernetes allocation').fill('3')
    mobile.get_by_role('button', name='Build my session →').click()
    assert mobile.locator('#interview-deck').is_visible()
    assert mobile.locator('#session-progress').inner_text() == '1 / 6'
    mobile.get_by_role('button', name='Reveal answer link').click()
    answer_link = mobile.locator('#session-answer a')
    assert answer_link.is_visible()
    assert answer_link.get_attribute('href').endswith('.html')
    mobile.get_by_role('button', name='Next →').click()
    assert mobile.locator('#session-progress').inner_text() == '2 / 6'
    session_params = mobile.evaluate('Object.fromEntries(new URLSearchParams(location.search))')
    assert set(session_params['themes'].split(',')) == {'linux', 'kubernetes'}
    assert session_params['total'] == '6' and session_params['index'] == '1'
    assert set(session_params['allocations'].split(',')) == {'linux:3', 'kubernetes:3'}
    mobile.close()
    browser.close()
