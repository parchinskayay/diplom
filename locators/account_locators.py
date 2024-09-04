from selenium.webdriver.common.by import By


class AccountPageLocators:
    BUTTON_ACCOUNT = (By.CSS_SELECTOR, '[class="styles_userToolsToggler__c2aHe"]')
    BUTTON_ENTER = (By.CSS_SELECTOR, '[data-testid="loginButton"]')

    CHECK_EMAIL = (By.CLASS_NAME, 'ErrorMessage-module__message')
    FIELD_EMAIL = (By.XPATH, '//input[@label="Электронная почта"]')
    FIELD_PASSW = (By.XPATH, '//input[@label="Пароль"]')
    EMAIL_FIELD_EMPTY = (By.CSS_SELECTOR, '[class$="6og5"] [class$="module__error"]')
    EMAIL_FIELD_EMPTY2 = (By.CSS_SELECTOR, '[class="ErrorMessage-module__message"]')
    PASSW_FIELD_EMPTY = (By.CSS_SELECTOR, '[class="FieldWrapper-module__wrapper"] '
                                          '[class$="module__message"]')
    PASSW_FIELD_EMPTY2 = (By.CSS_SELECTOR, '[ErrorMessage-module__message]')
    FIELD_RESET_PASSW_EMAIL = (By.XPATH, '//input[@label="Электронная почта"]')
    BUTTON_SEND = (By.XPATH, '//button[@class="Button-module__button Button-module__blue-primary"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[class="SuccessScreen_successMessageWrapper___Hk_F"]')

    INCORRECT_PASSW = (By.CSS_SELECTOR, '[class="styles_errorText__LEN7M"]')
    INCORRECT_PASSW2 = (By.CSS_SELECTOR, '[class="ErrorMessageLink_container__7D0yM"]')
    BUTTON_RESET_PASSW = (By.CSS_SELECTOR, '[class="styles_errorText__LEN7M"] '
                                           '[class="Button-module__buttonText"]')
    BUTTON_RESET_PASSW2 = (By.CSS_SELECTOR, '[class="Button-module__button '
                                            'ErrorMessageLink_link__JKDLX Button-module__blue-inline"]')
    RESET_PASSW_FORM = (By.CSS_SELECTOR, '[class="Form-module__formTitle"]')
    BUTTON_FORGOT_PASSW = (By.XPATH, '//*[contains(text(),"Забыли пароль")]')
    BUTTON_SUBMIT = (By.CSS_SELECTOR, '[data-testid="loginSubmit"]')

    BUTTON_REGISTRATION = (By.CSS_SELECTOR, '[class$="styles_secondaryAction__H7V7H"]')
    BUTTON_REGISTRATION2 = (By.CSS_SELECTOR, '[class="Button-module__button Button-module__blue-inline"]')
    FIELD_REG_TEL_NUMBER = (By.XPATH, '//input[@label="Номер телефона"]')
    FIELD_REG_EMAIL = (By.XPATH, '//input[@label="Электронная почта"]')
    BUTTON_CONFIRM_REGISTRATION = (By.CSS_SELECTOR, '[class="Button-module__button Button-module__blue-primary"]')
    INCORRECT_EMAIL_REGISTRATION = (By.CSS_SELECTOR, '[class="ErrorMessage-module__message"]')
    BUTTON_CONTINUE = (By.XPATH, '//div[contains(text(),"Продолжить")]')
    BUTTON_AGREE_PER_DATA = (By.XPATH, '//div[contains(text(),"Соглашаюсь")]')
    FIELD_CHECK_EMAIL_OR_LOGIN = (By.CSS_SELECTOR, '[class="ErrorMessageLink_container__7D0yM"]')
    FIELD_CHECK_EMAIL_OR_LOGIN2 = (By.CSS_SELECTOR, '[class="styles_errorText__LEN7M"]')
