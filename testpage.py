from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:

    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_LOGIN_RESULT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITTLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH,"""//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_POST_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button/span""")
    LOCATOR_SAVE_POST_RESULT = (By.CSS_SELECTOR, """#app > main > div > div.container.svelte-tv8alb > h1""")
    LOCATOR_PROFILE_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_LOGOUT_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/div/ul/li[3]""")
    LOCATOR_CONTACT_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info(f'Click to element {TestSearchLocators.LOCATOR_LOGIN_BTN[1]}')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f'We find {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_result_auth(self):
        result_auth = self.find_element(TestSearchLocators.LOCATOR_LOGIN_RESULT, time=3)
        text = result_auth.text
        logging.info(f'We find {text} in error field {TestSearchLocators.LOCATOR_LOGIN_RESULT[1]}')
        return text

    def click_create_post_button(self):
        logging.info(f'Click to element {TestSearchLocators.LOCATOR_CREATE_POST_BTN[1]}')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def create_tittle_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_TITTLE_FIELD[1]}')
        tittle_field = self.find_element(TestSearchLocators.LOCATOR_TITTLE_FIELD)
        tittle_field.clear()
        tittle_field.send_keys(word)

    def create_description_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)


    def create_content_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_button_save_post(self):
        logging.info(f'Click to element {TestSearchLocators.LOCATOR_SAVE_POST_BTN[1]}')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_result_public_post(self):
        result_save_post = self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_RESULT, time=3)
        text = result_save_post.text
        logging.info(f'We find {text} in tittle {TestSearchLocators.LOCATOR_SAVE_POST_RESULT[1]}')
        return text

    def click_contact(self):
        logging.info(f'Click to element {TestSearchLocators.LOCATOR_CONTACT_FIELD[1]}')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_FIELD).click()

    def enter_name_to_contact_us(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email_to_contact_us(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def enter_content_to_contact_us(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}')
        name_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        name_field.clear()
        name_field.send_keys(word)

    def click_contact_us_btn(self):
        logging.info(f'Click to element {TestSearchLocators.LOCATOR_CONTACT_US_BTN[1]}')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def checkout_alert(self):
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        logging.info(f'We find {text} in alert when click to {TestSearchLocators.LOCATOR_CONTACT_US_BTN[1]}')
        return text

    def log_out(self):
        self.find_element(TestSearchLocators.LOCATOR_PROFILE_FIELD).click()
        self.find_element(TestSearchLocators.LOCATOR_LOGOUT_FIELD).click()

    def get_result_login_out(self):
        result_login_out = self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN, time=3)
        text = result_login_out.text
        logging.info(f'We find {text} in error field {TestSearchLocators.LOCATOR_LOGIN_BTN[1]}')
        return text
