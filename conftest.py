import pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser =="chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\zeyne\\PycharmProjects\\Pytest_Framework\\direvers\\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Users\\zeyne\\PycharmProjects\\Pytest_Framework\\direvers\\geckodriver.exe")
    driver.implicitly_wait(15)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("test completed")