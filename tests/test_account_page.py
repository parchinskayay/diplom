from pages.main_page import MainPage
from pages.account_page import AccountPage


def test_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.incorrect_email()


def test_incorrect_password(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.incorrect_password()


def test_field_email_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.field_email_is_empty()


def test_field_passw_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.field_passw_is_empty()


def test_forgot_passw(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.forgot_passw()


def test_reset_password(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.reset_password()


def test_check_that_user_is_already_exist(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    account_page = AccountPage(driver)
    account_page.check_that_user_is_already_exist()
