from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.welcome_button_css_selector = ".oxd-userdropdown-name"
        self.logout_link_test = "Logout"
    def click_welcome(self):
        self.driver.find_element(By.CSS_SELECTOR, self.welcome_button_css_selector).click()
    def clcik_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_test).click()