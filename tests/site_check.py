import json
from pathlib import Path
from playwright.sync_api import sync_playwright

site = Path('index.html').resolve().as_uri()
manifest = json.loads(Path('config/content-manifest.json').read_text(encoding='utf-8'))
certifications = manifest['certifications']

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

    # Hash navigation also works at a narrow touch viewport.
    mobile = browser.new_page(viewport={"width": 390, "height": 844})
    mobile.goto(f'{site}#certificate=lfcs')
    mobile.wait_for_load_state('networkidle')
    lfcs_count = mobile.evaluate("window.questions.filter((question) => question.tags.includes('lfcs')).length")
    assert mobile.locator('.question-card').count() == lfcs_count
    assert mobile.locator('#certification-filters button[data-certificate="lfcs"]').get_attribute('aria-pressed') == 'true'
    mobile.close()
    browser.close()
