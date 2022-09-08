import allure
import moment
from selenium.webdriver import Firefox
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils



@pytest.mark.usefixtures("test_setup")
class TestLogin():
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
    def test_log_out(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.clcik_logout()
            title = driver.title
            assert title == "Orange"
        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:\\Users\\zeyne\\PycharmProjects\\Pytest_Framework\\screenshot\\"+ screenshotName+ ".png")

            raise
        except:
            print("There was an exception in test_logout function")
            raise
        else:
            print("No exceptions occured")
        finally:
            print("I am inside the finally block")

# 1. html report
# to take html reports we need to write this command on the terminal
# python -m pytest --html=reports/report1.html tests/tests_login.py
# then a report folder will appear in our project

# 2. allure report
# python -m  pytest --alluredir=reports/allure-reports tests/tests_login.py
# to see report
# allure serve reports/allure-reports tests/tests_login.py
#ctrl + c  to exit from report
