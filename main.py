import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    expect(page.get_by_role('link', name='Continue')).to_be_visible()
    page.get_by_role("link", name="Continue").click()


    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)

