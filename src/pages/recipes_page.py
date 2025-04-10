from selenium.webdriver.common.by import By
import allure
from .base_page import BasePage
from src.helpers import URLS, get_russian_letter, get_number


class RecipesPage(BasePage):
    RECIPES_TAB = (By.XPATH, "//a[text()='Рецепты']")
    CREATE_RECIPE_TAB = (By.XPATH, "//a[text()='Создать рецепт']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    RECIPE_NAME_INPUT = (By.XPATH, "//div[text()='Название рецепта']/../input")
    INGREDIENTS_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/../input")
    INGREDIENTS_POPUP_LIST = (By.XPATH, "//div[@class='styles_container__3ukwm']/div")
    INGREDIENTS_AMOUNT_VALUE = (By.XPATH, "//input[contains(@class, 'ingredientsAmountValue')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    RECIPE_IMAGE_INPUT = (By.XPATH, "//label[text()='Загрузить фото']/../input")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/../input")
    RECIPE_DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/../textarea")
    RECIPE_TITLE = (By.XPATH, "//h1")

    @allure.step("Переход на страницу «Создать рецепт»")
    def get_recipes_page(self):
        self.get_page(URLS.RECIPES_PAGE)

    @allure.step("Клик по вкладке «Создать рецепт»")
    def click_on_create_recipe_tab(self):
        self.click_on(self.CREATE_RECIPE_TAB)
        self.wait_for_element_to_be_visible(self.CREATE_RECIPE_BUTTON)

    @allure.step("Ввод текста в поле «Название рецепта»")
    def fill_recipe_name_field(self, text):
        self.send_keys(self.RECIPE_NAME_INPUT, text)

    @allure.step("Ввод текста в поле «Ингредиенты»")
    def fill_ingredients_field(self, text):
        self.send_keys(self.INGREDIENTS_INPUT, text)

    @allure.step("Выбор случайного ингредиента из списка")
    def click_on_random_ingredient_from_popup_list(self):
        self.wait_for_element_to_be_visible(self.INGREDIENTS_POPUP_LIST)
        ingredients_list = self.find_elements(self.INGREDIENTS_POPUP_LIST)
        ingredient_index = get_number(0, len(ingredients_list) - 1)
        self.scroll_to_element(ingredients_list[ingredient_index])

        with allure.step('Данные теста'):
            allure.attach(str(ingredients_list[ingredient_index].text), name='ingredient_name')

        ingredients_list[ingredient_index].click()

    @allure.step("Ввод количества ингредиента")
    def fill_ingredient_amount_value(self, text):
        self.send_keys(self.INGREDIENTS_AMOUNT_VALUE, text)

    @allure.step("Клик по кнопке «Добавить ингредиент»")
    def click_on_add_ingredient_button(self):
        self.click_on(self.ADD_INGREDIENT_BUTTON)

    @allure.step("Добавление случайного ингредиента")
    def add_random_ingredient(self):
        # выбор ингредиента по первой букве
        start_letter = get_russian_letter()
        self.fill_ingredients_field(start_letter)
        self.click_on_random_ingredient_from_popup_list()
        # ввод массы ингредиента
        amount_value = str(get_number(1, 999))
        self.fill_ingredient_amount_value(amount_value)
        # добавить ингредиент
        self.click_on_add_ingredient_button()

    @allure.step("Указание времени приготовления")
    def set_cooking_time(self, text):
        self.send_keys(self.COOKING_TIME_INPUT, text)

    @allure.step("Загрузка тестовой картинки рецепта")
    def upload_picture_to_recipe(self, picture_link):
        self.make_element_visible(self.RECIPE_IMAGE_INPUT)
        self.send_keys(self.RECIPE_IMAGE_INPUT, picture_link)

    @allure.step("Добавление описания рецепта")
    def set_recipe_description(self, text):
        self.send_keys(self.RECIPE_DESCRIPTION_INPUT, text)

    @allure.step("Заполнение полей рецепта")
    def fill_recipe_fields(self, recipe_data):
        self.fill_recipe_name_field(recipe_data['recipe_name'])
        for _ in range(recipe_data['ingredients_number']):
            self.add_random_ingredient()
        self.set_cooking_time(recipe_data['cooking_time'])
        self.upload_picture_to_recipe(recipe_data['picture_link'])
        self.set_recipe_description(recipe_data['recipe_description'])

    @allure.step("Клик по кнопке «Создать рецепт»")
    def click_on_create_recipe_button(self):
        self.click_on(self.CREATE_RECIPE_BUTTON)
        self.wait_for_element_to_be_visible(self.CREATE_RECIPE_BUTTON)

    @allure.step("Создание рецепта")
    def create_recipe(self, recipe_data):
        self.fill_recipe_fields(recipe_data)
        self.click_on_create_recipe_button()
        self.wait_for_url_matches(URLS.READY_RECIPE_URL_PATTERN)

    @allure.step("Извлечение имени рецепта")
    def get_recipe_title(self):
        self.wait_for_element_to_be_visible(self.RECIPE_TITLE)
        recipe_title = self.find_element(self.RECIPE_TITLE).text

        with allure.step('Данные теста'):
            allure.attach(str(recipe_title), name='recipe_title')

        return recipe_title
