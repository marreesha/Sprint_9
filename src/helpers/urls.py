from re import compile

class URLS:
    BASE_URL = 'https://foodgram-frontend-1.prakticum-team.ru'
    SIGNIN_PAGE = f'{BASE_URL}/signin'
    SIGNUP_PAGE = f'{BASE_URL}/signup'
    RECIPES_PAGE = f'{BASE_URL}/recipes'
    READY_RECIPE_URL_PATTERN = compile(rf"^{RECIPES_PAGE}/\d+/?$")
