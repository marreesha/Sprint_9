from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from src.helpers import URLS


class AuthorisationPage(BasePage):
    SIGNUP_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='last_name']")
    USER_NAME_FIELD = (By.XPATH, "//input[@name='username']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")

    @allure.step("Переход на страницу «Авторизации»")
    def get_signin_page(self):
        self.get_page(URLS.SIGNIN_PAGE)

    @allure.step("Клик по кнопке «Создать аккаунт» в шапке страницы")
    def click_on_signup_button(self):
        self.wait_for_element_to_be_clickable(self.SIGNUP_BUTTON)
        self.click_on(self.SIGNUP_BUTTON)
        self.wait_for_page(URLS.SIGNUP_PAGE)

    @allure.step("Заполнение полей регистрации")
    def fill_registration_fields(self, user_data):
        self.send_keys(self.FIRST_NAME_FIELD, user_data['first_name'])
        self.send_keys(self.LAST_NAME_FIELD, user_data['last_name'])
        self.send_keys(self.USER_NAME_FIELD, user_data['user_name'])
        self.send_keys(self.EMAIL_FIELD, user_data['email'])
        self.send_keys(self.PASSWORD_FIELD, user_data['password'])

    @allure.step("Клик по кнопке «Создать аккаунт»")
    def click_on_register_account(self):
        self.click_on(self.CREATE_ACCOUNT_BUTTON)

    @allure.step("Регистрация пользователя")
    def create_user(self, user_data):
        self.fill_registration_fields(user_data)
        self.click_on_register_account()
        self.wait_for_page(URLS.SIGNIN_PAGE)

    @allure.step("Заполнение полей авторизации")
    def fill_login_fields(self, user_data):
        self.send_keys(self.EMAIL_FIELD, user_data['email'])
        self.send_keys(self.PASSWORD_FIELD, user_data['password'])

    @allure.step("Клик по кнопке «Войти»")
    def click_on_login_to_account(self):
        self.click_on(self.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Вход в аккаунт")
    def login_to_account(self, user_data):
        self.fill_login_fields(user_data)
        self.click_on_login_to_account()
        self.wait_for_page(URLS.RECIPES_PAGE)

    @allure.step("Состояние кнопки «Выход»")
    def logout_is_visible(self):
        return self.find_element(self.LOGOUT_BUTTON).is_displayed()
