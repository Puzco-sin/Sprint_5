from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators


class TestListing:
    def test_unauthenticated_user_cannot_create_listing(self, driver):
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable(locators.POST_AD_BUTTON)).click()

        actual = wait.until(
            EC.visibility_of_element_located(
                locators.LISTING_AUTH_REQUIRED_HEADING
            )
        ).text.strip()
        expected = "Чтобы разместить объявление, авторизуйтесь"
        assert actual == expected

    def test_authenticated_user_can_create_listing(
        self, driver, existing_account, listing_title
    ):
        email, password = existing_account
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.element_to_be_clickable(locators.LOGIN_AND_REGISTER_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(
            email
        )
        wait.until(
            EC.visibility_of_element_located(locators.PASSWORD_INPUT)
        ).send_keys(password)
        wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON))

        wait.until(EC.element_to_be_clickable(locators.POST_AD_BUTTON)).click()
        wait.until(
            EC.visibility_of_element_located(locators.LISTING_TITLE_INPUT)
        ).send_keys(listing_title)
        wait.until(
            EC.visibility_of_element_located(locators.LISTING_DESCRIPTION_INPUT)
        ).send_keys("Объявление создано UI-автотестом")
        wait.until(
            EC.visibility_of_element_located(locators.LISTING_PRICE_INPUT)
        ).send_keys("1234")
        wait.until(
            EC.element_to_be_clickable(locators.LISTING_CATEGORY_DROPDOWN)
        ).click()
        wait.until(
            EC.element_to_be_clickable(locators.AUTO_CATEGORY_BUTTON)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.LISTING_CITY_DROPDOWN)).click()
        wait.until(
            EC.element_to_be_clickable(locators.MOSCOW_CITY_BUTTON)
        ).click()
        wait.until(
            EC.element_to_be_clickable(locators.NEW_CONDITION_LABEL)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.PUBLISH_BUTTON)).click()
        wait.until(lambda browser: "/create-lisiting" not in browser.current_url)
        wait.until(EC.element_to_be_clickable(locators.POST_AD_BUTTON))
        wait.until(EC.element_to_be_clickable(locators.USER_AVATAR_BUTTON)).click()
        wait.until(EC.url_contains("/profile"))
        wait.until(EC.visibility_of_element_located(locators.MY_LISTINGS_HEADING))

        actual = wait.until(
            EC.visibility_of_element_located(locators.my_listing_title(listing_title))
        ).text.strip()
        expected = listing_title
        assert actual == expected
