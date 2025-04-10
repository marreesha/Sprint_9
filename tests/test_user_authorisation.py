import allure
from src import AuthorisationPage, URLS


@allure.feature('Авторизация пользователя')
class TestAuthorisation:

    @allure.story("Успешная авторизация пользователя")
    def test_authorisation(self, driver, register_user):
        page = AuthorisationPage(driver)
        page.login_to_account(register_user)

        assert page.get_current_url() == URLS.RECIPES_PAGE
        assert page.logout_is_visible() is True
