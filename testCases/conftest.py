from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest
from datetime import datetime
import os


# Webdriver & Browsers setup
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.maximize_window() 
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


# HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'BookSwappers'
    config._metadata['Tester'] = 'Dessy'

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = 'Reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
