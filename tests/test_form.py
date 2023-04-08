from pages.form_page import FormPage
from utils.selenium_utils import open_browser, close_browser


def test_form():
    # Opens the browser
    driver = open_browser()

    # Navigates to form page
    page = FormPage(driver)
    page.go_to()

    # Add name to First Name input
    page.input_first_name().send_keys("Jason")

    # Closes the browser
    close_browser(driver)
