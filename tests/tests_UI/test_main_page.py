from pages.main_page import MainPage
import pytest
import allure


@allure.title('Reject cookies')
def test_that_cookies_is_rejected_and_closed(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    main_page.assert_that_cookies_doesnt_exist()


@allure.title('Accept cookies')
def test_that_cookies_is_accepted_and_closed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()

    main_page.assert_that_cookies_doesnt_exist()


@allure.title('Close dropdown window')
def test_that_dropdown_window_about_sales_is_closed(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.click_agree_cookies()
    main_page.close_dropdown_window_about_sales()

    main_page.assert_that_dropdown_window_about_sales_is_closed()


@allure.title('Main banner exist')
def test_that_banner_is_displayed(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    main_page.assert_that_banner_is_displayed()


@allure.title('Logo exist')
def test_that_logo_is_displayed(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    main_page.assert_that_logo_is_displayed()


@allure.title('Contact center opening hours exist')
def test_contact_center_opening_hours_are_displayed(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    main_page.assert_contact_center_opening_hours_are_displayed()


@allure.title('The "add to cart" button has the text')
def test_that_first_element_button_has_text_in_basket(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    main_page.assert_that_product_button_has_text_in_basket_by_index(0)


@allure.title('Bonus program exist')
def test_click_bonus_program(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_bonus_program()

    main_page.assert_that_bonus_program_baner_is_exist()


@allure.title('Partly pay exist')
def test_click_partly_pay(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_partly_pay()

    main_page.assert_partly_payment_banner_is_exist()


@allure.title('Search field is working')
def test_search_field_is_working(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_search_headphones()

    main_page.assert_that_headphones_are_exist()


@pytest.mark.parametrize("city", ["г. Брест", "г. Гомель", "г. Витебск"])
@allure.title('Change city')
def test_change_city(driver, city):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.change_city(city)

    main_page.assert_city_on_main_page(city)


@pytest.mark.parametrize("sale_value", [50, 40, 30, 20, 10])
@allure.title('Check sale filter')
def test_check_sale_filter(driver, sale_value):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_all_promotions()
    main_page.set_filter_value(sale_value)
    main_page.click_apply_sale_filter()

    main_page.assert_sale_vale_of_first_product_in_filtered_products(sale_value)


@allure.title('Button show more')
def test_assert_show_more_button(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    count_popular_els_old = main_page.get_count_popular_elements()
    main_page.click_show_more_popular_elements()
    count_popular_els_new = main_page.get_count_popular_elements()

    assert count_popular_els_old < count_popular_els_new


@allure.title('Popular filter cheap')
def test_check_popular_filter_cheap(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_less_than_on_popular_products()

    main_page.assert_first_froduct_of_populars_is_filtered()


@allure.title('Button write us')
def test_check_write_to_us_button(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_write_to_us()

    main_page.assert_feedback_window_is_exist()


@allure.title('Subscription form is empty')
def test_check_subscription_form_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.click_input_email_in_subscription_form()

    main_page.assert_that_email_is_not_specified_in_subscription_form()


@allure.title('Subscription form with incorrect email')
def test_check_subscription_form_incorrect_email(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.set_email_in_subscription_form('1111')
    main_page.click_input_email_in_subscription_form()

    main_page.assert_incorrect_format_email_in_subscription_form()


@allure.title('Subscription form work with correct email')
def test_check_subscription_form_work_correct(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.set_email_in_subscription_form('example@example.com')
    main_page.click_input_email_in_subscription_form()

    main_page.assert_that_open_account_page()


@allure.title('Button up')
def test_check_button_up(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.scroll_to_bottom()
    main_page.click_up_button()

    main_page.assert_that_now_is_window_top()
