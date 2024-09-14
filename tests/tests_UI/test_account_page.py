from pages.account_page import AccountPage
from pages.main_page import MainPage
import allure


@allure.title('Incorrect email message')
def test_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email('1111')
    account_page.set_password('12345')
    account_page.click_submit_button()

    account_page.assert_incorrect_email_message()


@allure.title('Incorrect password message')
def test_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email('example@example.com')
    account_page.set_password('12345')
    account_page.click_submit_button()

    account_page.assert_incorrect_password_message()


@allure.title('Field email is empty message')
def test_field_email_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_password('12345')
    account_page.click_submit_button()

    account_page.assert_empty_email_message()


@allure.title('Field passw is empty message')
def test_field_passw_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email('example@example.com')
    account_page.click_submit_button()

    account_page.assert_empty_password_message()


@allure.title('Button reset message')
def test_forgot_password(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.click_forgot_password()
    account_page.set_email_reset_form('example@example.com')
    account_page.click_send_reset_message()

    account_page.assert_success_reset_message()


@allure.title('Reset password form is exist')
def test_reset_password(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.set_email('example@example.com')
    account_page.set_password('12345')
    account_page.click_submit_button()
    account_page.click_reset_password()

    account_page.assert_reset_passwort_form_is_exist()


@allure.title('Incorrect email registration')
def test_registration_that_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.click_registration()
    account_page.set_email_in_registration('1111')
    account_page.set_phone_number_in_registration_if_necessary('290000000')
    account_page.click_confirm_registration_if_necessary()

    account_page.assert_email_is_incorrect_in_registration()


@allure.title('User is already exist')
def test_registration_that_user_is_already_exist(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    account_page = AccountPage(driver)
    account_page.open_account_page()
    account_page.click_registration()
    account_page.set_phone_number_in_registration_if_necessary('290000000')
    account_page.set_email_in_registration('example@example.com')
    account_page.click_continue_registration()
    account_page.agree_to_processing_of_personal_data_if_necessary()

    account_page.assert_check_email_message_in_registration()
