from playwright.sync_api import sync_playwright

BASE_URL = "http://144.31.63.127:5000/"
INVALID_LOGIN_ERROR = "Invalid login or password."


def login(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)
        button = page.locator("text = Login")
        button.click()
        page.fill("#username", username)
        page.fill("#password", password)
        button = page.locator("text = Confirm")
        button.click()

        page.wait_for_selector(".button-spinner", state="visible")
        page.wait_for_selector(".button-spinner", state="hidden")

        error = page.get_by_text(INVALID_LOGIN_ERROR).text_content()

        browser.close()
        
        return error