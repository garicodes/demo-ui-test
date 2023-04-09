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

    # Add email to Email Address input
    page.input_user_email().send_keys("jvoorhees@slasher.pro")

    # Choose gender
    page.label_male().click()
    page.label_female().click()
    page.label_other().click()

    # Choosing date of birth
    page.select_month().click()
    page.option_june().click()
    page.select_year()

    # Closes the browser
    close_browser(driver)
