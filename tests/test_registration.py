from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators


class TestRegistration:
    def test_register_user(self, driver, generated_email, new_user_password):
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.element_to_be_clickable(locators.LOGIN_AND_REGISTER_BUTTON)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(
            generated_email
        )
        wait.until(
            EC.visibility_of_element_located(locators.PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.visibility_of_element_located(locators.REPEAT_PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON))

        actual = (
            driver.find_element(*locators.LOGOUT_BUTTON).is_displayed(),
            driver.find_element(*locators.USER_AVATAR_BUTTON).is_displayed(),
        )
        expected = (True, True)
        assert actual == expected

    def test_register_invalid_email(self, driver, new_user_password):
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.element_to_be_clickable(locators.LOGIN_AND_REGISTER_BUTTON)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()

        wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(
            "invalid-email"
        )
        wait.until(
            EC.visibility_of_element_located(locators.PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.visibility_of_element_located(locators.REPEAT_PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(locators.INVALID_EMAIL_MESSAGE))

        actual = (
            [
                "inputError"
                in driver.find_element(*input_locator)
                .find_element(*locators.INPUT_WRAPPER)
                .get_attribute("class")
                for input_locator in locators.REGISTRATION_INPUTS
            ],
            driver.find_element(*locators.INVALID_EMAIL_MESSAGE).text.strip(),
        )
        expected = ([True, True, True], "Ошибка")
        assert actual == expected

    def test_register_existing_user(
        self, driver, generated_email, new_user_password
    ):
        wait = WebDriverWait(driver, 20)
        wait.until(
            EC.element_to_be_clickable(locators.LOGIN_AND_REGISTER_BUTTON)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(
            generated_email
        )
        wait.until(
            EC.visibility_of_element_located(locators.PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.visibility_of_element_located(locators.REPEAT_PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON))
        wait.until(EC.invisibility_of_element_located(locators.EMAIL_INPUT))
        wait.until(EC.element_to_be_clickable(locators.LOGOUT_BUTTON)).click()
        wait.until(
            EC.visibility_of_element_located(locators.LOGIN_AND_REGISTER_BUTTON)
        )

        wait.until(
            EC.element_to_be_clickable(locators.LOGIN_AND_REGISTER_BUTTON)
        ).click()
        wait.until(EC.element_to_be_clickable(locators.NO_ACCOUNT_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(locators.EMAIL_INPUT)).send_keys(
            generated_email
        )
        wait.until(
            EC.visibility_of_element_located(locators.PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.visibility_of_element_located(locators.REPEAT_PASSWORD_INPUT)
        ).send_keys(new_user_password)
        wait.until(
            EC.element_to_be_clickable(locators.CREATE_ACCOUNT_BUTTON)
        ).click()
        wait.until(EC.visibility_of_element_located(locators.INVALID_EMAIL_MESSAGE))

        actual = (
            [
                "inputError"
                in driver.find_element(*input_locator)
                .find_element(*locators.INPUT_WRAPPER)
                .get_attribute("class")
                for input_locator in locators.REGISTRATION_INPUTS
            ],
            driver.find_element(*locators.INVALID_EMAIL_MESSAGE).text.strip(),
        )
        expected = ([True, True, True], "Ошибка")
        assert actual == expected
