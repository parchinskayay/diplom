from pages.main_page import MainPage


def test_agree_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.assert_agree_cookies()


def test_close_dropdown_window_about_sales(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.close_dropdown_window_about_sales()


def test_that_banner_is_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.assert_that_banner_is_displayed()


def test_that_logo_is_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.assert_that_logo_is_displayed()


def test_contact_center_opening_hours_are_displayed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.contact_center_opening_hours()


def test_choose_the_first_product_and_add_to_basket(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.choose_the_first_product_and_add_to_basket()


def test_bonus_program_button_is_working(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.bonus_program_button_is_working()


def test_search_field_is_working(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.search_field_is_working()


def test_button_payment_in_parts_is_working(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.button_payment_in_parts_is_working()


def test_change_city(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.change_city()
