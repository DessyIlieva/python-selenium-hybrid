from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
    return driver