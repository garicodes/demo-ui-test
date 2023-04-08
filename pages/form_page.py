from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def go_to(self):
        self.driver.get(self.url)

    def input_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='firstName']")
