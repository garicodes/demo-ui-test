from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/automation-practice-form"

    def go_to(self):
        self.driver.get(self.url)

    def input_first_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='firstName']")

    def input_last_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='lastName']")

    def input_user_email(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='userEmail']")

    def label_male(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")

    def label_female(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']")

    def label_other(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-3']")

    def input_date_birth(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='dateOfBirthInput']")

    def select_month(self):
        return self.driver.find_element(By.CSS_SELECTOR, "select[class$='month-select']")

    def option_june(self):
        return self.driver.find_element(By.CSS_SELECTOR, "option[value='5']")

    def select_year(self):
        return self.driver.find_element(By.CSS_SELECTOR, "select[class$='year-select']")

    def option_specific_year(self):
        return self.driver.find_element(By.CSS_SELECTOR, "option[value='1946']")

    def choose_day(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[class='react-datepicker__day react-datepicker__day--013']")

    def label_custom(self):
        return self.driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-1']")

    def current_address(self):
        return self.driver.find_element(By.CSS_SELECTOR, "textarea[id='currentAddress']")

    def input_react_select(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id='react-select-3-input']")

    def div_state(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='state']")
