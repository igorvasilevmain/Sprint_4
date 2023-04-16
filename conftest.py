import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Firefox(executable_path='./geckodriver')
    yield browser
    browser.quit()
