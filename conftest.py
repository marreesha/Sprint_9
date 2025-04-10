import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from src import AuthorisationPage, generate_user_data


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--user-data-dir=/path/to/unique/directory")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture()
def register_user(driver):
    user_data = generate_user_data()
    page = AuthorisationPage(driver)
    page.get_signin_page()
    page.click_on_signup_button()
    page.create_user(user_data)
    return user_data


@pytest.fixture()
def login_user(driver, register_user):
    page = AuthorisationPage(driver)
    page.login_to_account(register_user)
