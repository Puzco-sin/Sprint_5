import os
import uuid

import pytest
from selenium import webdriver

import locators


BASE_URL = os.getenv("DESK_BASE_URL", "https://qa-desk.education-services.ru/")


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    try:
        browser.get(BASE_URL)
        yield browser
    finally:
        browser.quit()


@pytest.fixture
def generated_email():
    return f"ui-test-{uuid.uuid4().hex}@example.com"


@pytest.fixture
def new_user_password():
    return os.getenv("DESK_NEW_USER_PASSWORD", "TestPassword123!")


@pytest.fixture
def listing_title():
    return f"UI тестовое объявление {uuid.uuid4().hex[:8]}"


@pytest.fixture
def existing_account():
    email = os.getenv("DESK_TEST_EMAIL", locators.TEST_ACCOUNT_EMAIL)
    password = os.getenv("DESK_TEST_PASSWORD", locators.TEST_ACCOUNT_PASSWORD)
    return email, password
