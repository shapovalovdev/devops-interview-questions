from pathlib import Path
from playwright.sync_api import sync_playwright

site = Path('index.html').resolve().as_uri()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto(site)
    page.wait_for_load_state('networkidle')
    cards = page.locator('.question-card')
    assert cards.count() == 27
    assert all(href.endswith('.html') for href in cards.locator('a').evaluate_all('(links) => links.map((link) => link.getAttribute("href"))'))
    page.locator('#search').fill('DNS')
    assert cards.count() == 2
    page.locator('#search').fill('')
    page.get_by_role('button', name='security').click()
    assert cards.count() == 1
    browser.close()
