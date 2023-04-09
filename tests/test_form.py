import time

from pages.form_page import FormPage
from utils.selenium_utils import open_browser, close_browser

# Defining the driver variable as a global variable
driver = None
page = None


def setup():
    # Open the browser before running tests
    global driver
    driver = open_browser()
    global page
    page = FormPage(driver)


def teardown():
    # Close the browser after running tests
    global driver
    close_browser(driver)


def test_form():
    # Navigates to form page
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
    page.input_date_birth().click()
    page.select_month().click()
    page.option_june().click()
    page.select_year().click()
    page.option_specific_year().click()
    page.choose_day().click()

    time.sleep(10)
    page.take_screenshot()

    # Closes the browser
    close_browser(driver)
