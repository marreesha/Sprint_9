import allure
from src import AuthorisationPage, URLS, generate_user_data


@allure.feature('Создание аккаунта')
class TestCreateAccount:

    @allure.story('Успешное создание аккаунта')
    def test_create_account(self, driver):
        page = AuthorisationPage(driver)
        page.get_signin_page()

        page.click_on_signup_button()
        user_data = generate_user_data()
        page.create_user(user_data)

        assert page.get_current_url() == URLS.SIGNIN_PAGE
