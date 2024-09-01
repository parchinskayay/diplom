from pages.main_page import MainPage


def init_main_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.click_close_dropdown_window()
    return main_page


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
    main_page = init_main_page(driver)
    main_page.assert_that_banner_is_displayed()


def test_that_logo_is_displayed(driver):
    main_page = init_main_page(driver)
    main_page.assert_that_logo_is_displayed()


def test_contact_center_opening_hours_are_displayed(driver):
    main_page = init_main_page(driver)
    main_page.contact_center_opening_hours()


def test_choose_the_first_product_and_add_to_basket(driver):
    main_page = init_main_page(driver)
    main_page.choose_the_first_product_and_add_to_basket()


def test_bonus_program_button_is_working(driver):
    main_page = init_main_page(driver)
    main_page.bonus_program_button_is_working()


def test_search_field_is_working(driver):
    main_page = init_main_page(driver)
    main_page.search_field_is_working()


def test_button_payment_in_parts_is_working(driver):
    main_page = init_main_page(driver)
    main_page.button_payment_in_parts_is_working()


def test_change_city(driver):
    main_page = init_main_page(driver)
    main_page.change_city()


def test_favorites_is_empty(driver):
    main_page = init_main_page(driver)
    main_page.favorites_is_empty()


def test_favorites_is_not_empty(driver):
    main_page = init_main_page(driver)
    main_page.favorites_is_not_empty()


def test_basket_is_empty(driver):
    main_page = init_main_page(driver)
    main_page.basket_is_empty()


def test_basket_is_not_empty(driver):
    main_page = init_main_page(driver)
    main_page.basket_is_not_empty()


def test_favorites_are_working(driver):
    main_page = init_main_page(driver)
    main_page.favorites_are_working()


def test_delete_from_favorites(driver):
    main_page = init_main_page(driver)
    main_page.delete_from_favorites()


def test_check_sale_filter(driver):
    main_page = init_main_page(driver)
    main_page.check_sale_filter()


def test_assert_show_more_button(driver):
    main_page = init_main_page(driver)
    main_page.assert_show_more_button()


def test_check_popular_filter_cheap(driver):
    main_page = init_main_page(driver)
    main_page.check_popular_filter_cheap()


def test_check_write_to_us_button(driver):
    main_page = init_main_page(driver)
    main_page.check_write_to_us_button()


def test_check_subscription_form_empty(driver):
    main_page = init_main_page(driver)
    main_page.check_subscription_form_empty()


def test_check_subscription_form_incorrect_email(driver):
    main_page = init_main_page(driver)
    main_page.check_subscription_form_incorrect_email()


def test_check_subscription_form_work_correct(driver):
    main_page = init_main_page(driver)
    main_page.check_subscription_form_work_correct()


def test_check_button_up(driver):
    main_page = init_main_page(driver)
    main_page.check_button_up()
