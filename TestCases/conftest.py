from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Chrome()
        return driver

def pytest_addoption(parser): #this will get the value from command line/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request): #this will return the browser valuevto setup method
    return request.config.getoption("--browser")