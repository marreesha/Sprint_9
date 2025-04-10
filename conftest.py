import pytest
import tempfile
from selenium import webdriver
from src import AuthorisationPage, generate_user_data


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    driver = webdriver.Chrome()
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
