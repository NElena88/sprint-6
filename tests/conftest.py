import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *
from pages.base_page import BasePage
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1200,600")
    browser = webdriver.Firefox()
    browser.get(main_site)
    yield browser
    browser.quit()