import re
from time import sleep
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.1mcs.ru/auth")
    expect(page.get_by_role("button", name="Войти")).to_be_visible()
    sleep(1)
    page.get_by_role("button", name="Войти").click()
    sleep(2)
    expect(page.locator("#error_msg")).to_contain_text("Такого пользователя нет!")
    sleep(1)
    expect(page.get_by_placeholder("Введите логин (email)")).to_be_visible()
    expect(page.get_by_role("textbox", name="Введите пароль")).to_be_visible()
    sleep(1)


    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)

