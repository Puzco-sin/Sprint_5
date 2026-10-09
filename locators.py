"""Selenium locators for the Desk UI tests."""

from selenium.webdriver.common.by import By


TEST_ACCOUNT_EMAIL = "sinev_qa38_1@yandex.ru"
TEST_ACCOUNT_PASSWORD = "12345678Aa"

LOGIN_AND_REGISTER_BUTTON = (
    By.XPATH,
    "//button[normalize-space()='Вход и регистрация']",
)
POST_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Разместить объявление']")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")
LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")
PUBLISH_BUTTON = (By.XPATH, "//button[normalize-space()='Опубликовать']")

EMAIL_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Введите Email"]')
PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Пароль"]')
REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Повторите пароль"]')
LISTING_TITLE_INPUT = (
    By.CSS_SELECTOR,
    'input[placeholder="Название"], textarea[placeholder="Название"]',
)
LISTING_DESCRIPTION_INPUT = (
    By.CSS_SELECTOR,
    'input[placeholder="Описание товара"], textarea[placeholder="Описание товара"]',
)
LISTING_PRICE_INPUT = (
    By.CSS_SELECTOR,
    'input[placeholder="Стоимость"], textarea[placeholder="Стоимость"]',
)

INVALID_EMAIL_MESSAGE = (By.XPATH, "//*[normalize-space()='Ошибка']")
LISTING_AUTH_REQUIRED_HEADING = (
    By.XPATH,
    "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']",
)
MY_LISTINGS_HEADING = (By.XPATH, "//*[normalize-space()='Мои объявления']")
USER_AVATAR_BUTTON = (
    By.XPATH,
    "//div[contains(@class, 'header_shell')]//button[contains(@class, 'circleSmall')]",
)
AUTO_CATEGORY_BUTTON = (By.XPATH, "//button[normalize-space()='Авто']")
MOSCOW_CITY_BUTTON = (By.XPATH, "//button[normalize-space()='Москва']")
NEW_CONDITION_LABEL = (By.XPATH, "//label[normalize-space()='Новый']")
INPUT_WRAPPER = (By.XPATH, "..")
LISTING_CATEGORY_DROPDOWN = (
    By.CSS_SELECTOR,
    'input[name="category"] + button',
)
LISTING_CITY_DROPDOWN = (By.CSS_SELECTOR, 'input[name="city"] + button')

REGISTRATION_INPUTS = (
    EMAIL_INPUT,
    PASSWORD_INPUT,
    REPEAT_PASSWORD_INPUT,
)


def my_listing_title(title):
    return By.XPATH, f"//h2[normalize-space()='{title}']"
