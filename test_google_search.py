import pytest
from selenium import webdriver
from selene.support.shared import browser
from selene import be, have
from selenium.webdriver import DesiredCapabilities

positive_search_string='selene'
positive_validation_string = 'Selene - User-oriented Web UI browser tests in Python'
negative_search_string='selene sadsDFsdfsdfSDFsdfSDFsdfkl;jkl;jkl;jkl;fyguruyi'
negative_validation_string = ''


@pytest.fixture(scope='session', autouse=True)
def before_all_config():
    url = 'http://127.0.0.1:4444/wd/hub'
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['screenResolution'] = "2560x1440x24"
    capabilities['enableVNC'] = True
    browser.set_driver(webdriver.Remote(url, capabilities))

def test_positive_search():
    search(positive_search_string,positive_validation_string)


def test_negative_search():
    search(negative_search_string, negative_validation_string)


def search(search_string, validation_string):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(search_string).press_enter()
    browser.element('[id="search"]').should(have.text(validation_string))
