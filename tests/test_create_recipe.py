import allure
import pytest
from src import RecipesPage, generate_recipe_data


@allure.feature('Создание рецепта')
class TestCreateRecipe:

    @allure.story('Успешное создание рецепта')
    @allure.title('Число ингредиентов: {ingredients_number}')
    @pytest.mark.parametrize('ingredients_number', [2, 6, 10])
    def test_create_recipe(self, driver, login_user, ingredients_number):
        recipe_data = generate_recipe_data()
        recipe_data['ingredients_number'] = ingredients_number

        page = RecipesPage(driver)
        page.click_on_create_recipe_tab()
        page.create_recipe(recipe_data)

        assert page.get_recipe_title() == recipe_data['recipe_name']
