from selenium import webdriver


def open_browser():
    # Creating instance of ChromeDriver
    driver = webdriver.Chrome()

    return driver


def screenshot(driver):
    driver.save_screenshot('C:/Users/Gariel/PycharmProjects/demo-ui-test/screenshots/test_form.png')


def close_browser(driver):
    # Setting driver to close
    driver.quit()
