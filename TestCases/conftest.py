from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
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

#**********************PyTest HTML Report***************
#It is hook for Addimg Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Nop Commerce'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Pooja'

#It is hook for delete/modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

