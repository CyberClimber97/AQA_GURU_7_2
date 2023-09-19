from selene import Config
from selene.support.shared import browser
from selenium import webdriver
import pytest


options = webdriver.FirefoxOptions()


@pytest.fixture(scope="module")
def open_browser():
    browser.open('https://google.com')

    yield

    pass


@pytest.fixture(scope="module")
def browser_size():
    Config.window_width = 1920
    Config.window_height = 1080

