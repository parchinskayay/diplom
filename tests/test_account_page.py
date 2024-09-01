from pages.account_page import AccountPage
from test_main_page import init_main_page


def test_check_incorrect_email(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.check_incorrect_email()


def test_check_incorrect_password(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.check_incorrect_password()


def test_field_email_is_empty(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.field_email_is_empty()


def test_field_passw_is_empty(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.field_passw_is_empty()


def test_forgot_passw(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.forgot_passw()


def test_check_button_reset_password(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.check_button_reset_password()


def test_check_that_user_is_already_exist(driver):
    init_main_page(driver)

    account_page = AccountPage(driver)
    account_page.check_that_user_is_already_exist()
