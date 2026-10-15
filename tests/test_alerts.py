from pages.alerts_page import AlertsPage
from faker import Faker


def test_alerts_page(page):
    url = "http://the-internet.herokuapp.com/javascript_alerts"
    fake = Faker()
    text = fake.word()

    alerts_page = AlertsPage(page)
    alerts_page.open(url)
    alert_text = alerts_page.accept_alert()
    assert alert_text == "I am a JS Alert"
    assert alerts_page.get_result() == "You successfully clicked an alert"

    confirm_text = alerts_page.accept_confirm()
    assert confirm_text == "I am a JS Confirm"
    assert alerts_page.get_result() == "You clicked: Ok"

    prompt_text = alerts_page.accept_prompt(text)
    assert prompt_text == "I am a JS prompt"
    assert alerts_page.get_result() == f"You entered: {text}"
