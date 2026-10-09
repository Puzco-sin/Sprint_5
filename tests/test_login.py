from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators


class TestLogin:
    def test_login_user(self, driver, existing_account):
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

        actual = (
            driver.find_element(*locators.LOGOUT_BUTTON).is_displayed(),
            driver.find_element(*locators.USER_AVATAR_BUTTON).is_displayed(),
        )
        expected = (True, True)
        assert actual == expected
