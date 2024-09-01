from locators.account_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage, AccountPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_account_field(self):
        self.click(self.BUTTON_ACCOUNT)
        self.click(self.BUTTON_ENTER)

    def incorrect_email(self):
        self.open_account_field()
        self.wait_for(self.FIELD_EMAIL)
        self.fill(self.FIELD_EMAIL, 'example@1111')
        self.fill(self.FIELD_PASSW, '12345')
        self.click(self.BUTTON_SUBMIT)
        self.assertions.assert_that_element_is_visible(self.CHECK_EMAIL)

    def incorrect_password(self):
        self.open_account_field()
        self.wait_for(self.FIELD_EMAIL)
        self.fill(self.FIELD_EMAIL, 'example@example.com')
        self.fill(self.FIELD_PASSW, '12345')
        self.click(self.BUTTON_SUBMIT)
        if self.check_element_is_exist(self.INCORRECT_PASSW):
            self.assertions.assert_that_element_is_visible(self.INCORRECT_PASSW)
        else:
            self.assertions.assert_that_element_is_visible(self.INCORRECT_PASSW2)



    def field_email_is_empty(self):
        self.open_account_field()
        self.fill(self.FIELD_PASSW, '12345')
        self.click(self.BUTTON_SUBMIT)
        if self.check_element_is_exist(self.EMAIL_FIELD_EMPTY):
            self.assertions.assert_that_element_is_visible(self.EMAIL_FIELD_EMPTY)
        else:
            self.assertions.assert_that_element_is_visible(self.EMAIL_FIELD_EMPTY2)

    def field_passw_is_empty(self):
        self.open_account_field()
        self.fill(self.FIELD_EMAIL, 'example@example.com')
        self.click(self.BUTTON_SUBMIT)
        if self.check_element_is_exist(self.PASSW_FIELD_EMPTY):
            self.assertions.assert_that_element_is_visible(self.PASSW_FIELD_EMPTY)
        else:
            self.assertions.assert_that_element_is_visible(self.PASSW_FIELD_EMPTY2)

    def forgot_passw(self):
        self.open_account_field()
        self.click(self.BUTTON_FORGOT_PASSW)
        self.fill(self.FIELD_RESET_PASSW_EMAIL, 'example@example.com')
        self.click(self.BUTTON_SEND)
        self.wait_for(self.SUCCESS_MESSAGE)
        self.assertions.assert_that_element_is_visible(self.SUCCESS_MESSAGE)

    def reset_password(self):
        self.incorrect_password()
        self.click(self.BUTTON_SUBMIT)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_RESET_PASSW)

    def check_that_user_is_already_exist(self):
        self.open_account_field()

        self.click(self.BUTTON_REGISTRATION)
        if self.check_element_is_exist(self.FIELD_REG_TEL_NUMBER):
            self.fill(self.FIELD_REG_TEL_NUMBER, '290000000')
        self.fill(self.FIELD_REG_EMAIL, 'example@example.com')
        self.click(self.BUTTON_CONTINUE)
        if self.check_element_is_exist(self.BUTTON_AGREE_PER_DATA):
            self.click(self.BUTTON_AGREE_PER_DATA)
        if self.check_element_is_exist(self.FIELD_CHECK_EMAIL_OR_LOGIN):
            self.assertions.assert_that_element_is_visible(self.FIELD_CHECK_EMAIL_OR_LOGIN)
        else:
            self.assertions.assert_that_element_is_visible(self.FIELD_CHECK_EMAIL_OR_LOGIN2)


