from pages.main_page import HeadersElements


def test_agree_cookies(driver):
    main_page = HeadersElements(driver)
    main_page.click_agree_cookies()


def test_close_dropdown_window_about_sales(driver):
    main_page = HeadersElements(driver)
    main_page.close_dropdown_window_about_sales()


def test_that_banner_is_displayed(driver):
    main_page = HeadersElements(driver)
    main_page.assert_that_banner_is_displayed()


def test_that_logo_is_displayed(driver):
    main_page = HeadersElements(driver)
    main_page.assert_that_banner_is_displayed()


def test_choose_the_first_product_and_add_to_basket(driver):
    main_page = HeadersElements(driver)
    main_page.choose_the_first_product_and_add_to_basket()


def test_contact_center_opening_hours_are_displayed(driver):
    main_page = HeadersElements(driver)
    main_page.contact_center_opening_hours()

