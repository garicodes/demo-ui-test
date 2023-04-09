from selenium import webdriver


def open_browser():
    # Creating instance of ChromeDriver
    driver = webdriver.Chrome()

    return driver





def close_browser(driver):
    # Setting driver to close
    driver.quit()
