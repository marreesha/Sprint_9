from faker import Faker
import random
from .constants import TEST_PICTURE


def generate_user_data():
    fake = Faker('en-us')
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'user_name': fake.user_name(),
        'email': fake.email(),
        'password': fake.password()
    }


def generate_recipe_data():
    return {
        'recipe_name': 'Тестовый рецепт',
        'recipe_description': 'Тестовое описание тестового рецепта',
        'cooking_time': str(get_number(10, 120)),
        'ingredients_number': 4,
        'picture_link': TEST_PICTURE
    }


def get_russian_letter():
    valid_russian_letters = (
        'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'э', 'я'
    )
    return random.choice(valid_russian_letters)


def get_number(start=0, stop=1):
    return random.randint(start, stop)
