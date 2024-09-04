from locators.account_locators import AccountPageLocators
from pages.base_page import BasePage
import allure


class AccountPage(BasePage, AccountPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open account page')
    def open_account_page(self):
        self.click(self.BUTTON_ACCOUNT)
        self.click(self.BUTTON_ENTER)

    @allure.step('Set email')
    def set_email(self, email):
        self.fill(self.FIELD_EMAIL, email)

    @allure.step('Set password')
    def set_password(self, pw):
        self.fill(self.FIELD_PASSW, pw)

    @allure.step('Click submit button')
    def click_submit_button(self):
        self.click(self.BUTTON_SUBMIT)

    @allure.step('Assert incorrect email message')
    def assert_incorrect_email_message(self):
        self.assertions.assert_that_element_is_visible(self.CHECK_EMAIL)

    @allure.step('Assert incorrect password message')
    def assert_incorrect_password_message(self):
        if self.check_element_is_exist(self.INCORRECT_PASSW):
            self.assertions.assert_that_element_is_visible(self.INCORRECT_PASSW)
        else:
            self.assertions.assert_that_element_is_visible(self.INCORRECT_PASSW2)

    @allure.step('Assert empty email message')
    def assert_empty_email_message(self):
        if self.check_element_is_exist(self.EMAIL_FIELD_EMPTY):
            self.assertions.assert_that_element_is_visible(self.EMAIL_FIELD_EMPTY)
        else:
            self.assertions.assert_that_element_is_visible(self.EMAIL_FIELD_EMPTY2)

    @allure.step('Assert empty password message')
    def assert_empty_password_message(self):
        if self.check_element_is_exist(self.PASSW_FIELD_EMPTY):
            self.assertions.assert_that_element_is_visible(self.PASSW_FIELD_EMPTY)
        else:
            self.assertions.assert_that_element_is_visible(self.PASSW_FIELD_EMPTY2)

    @allure.step('Click forgot password')
    def click_forgot_password(self):
        self.click(self.BUTTON_FORGOT_PASSW)

    @allure.step('Set email reset form')
    def set_email_reset_form(self, email):
        self.fill(self.FIELD_RESET_PASSW_EMAIL, email)

    @allure.step('Click send reset message')
    def click_send_reset_message(self):
        self.click(self.BUTTON_SEND)

    @allure.step('Assert success reset message')
    def assert_success_reset_message(self):
        self.assertions.assert_that_element_is_visible(self.SUCCESS_MESSAGE)

    @allure.step('Click reset password')
    def click_reset_password(self):
        if self.check_element_is_exist(self.BUTTON_RESET_PASSW):
            self.click(self.BUTTON_RESET_PASSW)
        else:
            self.click(self.BUTTON_RESET_PASSW2)

    @allure.step('Assert reset passwort form is exist')
    def assert_reset_passwort_form_is_exist(self):
        self.assertions.assert_that_text_is_the_same(self.RESET_PASSW_FORM, 'Сброс пароля')

    @allure.step('Click registration')
    def click_registration(self):
        if self.check_element_is_exist(self.BUTTON_REGISTRATION):
            self.click(self.BUTTON_REGISTRATION)
        else:
            self.click(self.BUTTON_REGISTRATION2)

    @allure.step('Set phone number in registration if necessary')
    def set_phone_number_in_registration_if_necessary(self, number):
        if self.check_element_is_exist(self.FIELD_REG_TEL_NUMBER):
            self.fill(self.FIELD_REG_TEL_NUMBER, number)

    @allure.step('Set email in registration')
    def set_email_in_registration(self, email):
        self.fill(self.FIELD_REG_EMAIL, email)

    @allure.step('Click confirm registration if necessary')
    def click_confirm_registration_if_necessary(self):
        if self.check_element_is_exist(self.BUTTON_CONFIRM_REGISTRATION):
            self.click(self.BUTTON_CONFIRM_REGISTRATION)

    @allure.step('Assert email is incorrect in registration')
    def assert_email_is_incorrect_in_registration(self):
        self.assertions.assert_that_element_is_visible(self.INCORRECT_EMAIL_REGISTRATION)

    @allure.step('Click continue registration')
    def click_continue_registration(self):
        self.click(self.BUTTON_CONTINUE)

    @allure.step('Agree to processing of personal data if necessary')
    def agree_to_processing_of_personal_data_if_necessary(self):
        if self.check_element_is_exist(self.BUTTON_AGREE_PER_DATA):
            self.click(self.BUTTON_AGREE_PER_DATA)

    @allure.step('Assert check email message in registration')
    def assert_check_email_message_in_registration(self):
        if self.check_element_is_exist(self.FIELD_CHECK_EMAIL_OR_LOGIN):
            self.assertions.assert_that_element_is_visible(self.FIELD_CHECK_EMAIL_OR_LOGIN)
        else:
            self.assertions.assert_that_element_is_visible(self.FIELD_CHECK_EMAIL_OR_LOGIN2)
