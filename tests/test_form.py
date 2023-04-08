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

    # Add name to Last Name input
    page.input_last_name().send_keys("Voorhees")

    # Closes the browser
    close_browser(driver)
