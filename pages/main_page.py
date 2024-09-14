import time
from helpers.url import BASE_URL
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class MainPage(BasePage, MainPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open main page')
    def open(self):
        self.open_page(BASE_URL)

    @allure.step('Click reject cookies')
    def click_reject_cookies(self):
        self.click(self.BUTTON_REJECT_COOKIES)
        self.click(self.BUTTON_REJECT_COOKIES_SECOND)

    @allure.step('Click agree cookies')
    def click_agree_cookies(self):
        self.click(self.BUTTON_AGREE_COOKIES)

    @allure.step('Open page and reject cookies')
    def open_page_and_reject_cookies(self):
        self.open()
        self.click_reject_cookies()

    @allure.step('Assert that cookies doesnt exist')
    def assert_that_cookies_doesnt_exist(self):
        self.wait_until_element_disappear(self.COOKIE_WINDOW)
        self.assertions.assert_that_element_doesnt_exist(
            self.COOKIE_WINDOW
        )

    @allure.step('Close dropdown window about sales')
    def close_dropdown_window_about_sales(self):
        self.click(self.BUTTON_CLOSE_DROPDOWN_WINDOW)

    @allure.step('Assert that dropdown window about sales is closed')
    def assert_that_dropdown_window_about_sales_is_closed(self):
        self.wait_until_element_disappear(self.DROPDOWN_WINDOW)
        self.assertions.assert_that_element_doesnt_exist(
            self.DROPDOWN_WINDOW
        )

    @allure.step('Assert that banner is displayed')
    def assert_that_banner_is_displayed(self):
        self.assertions.assert_that_element_is_visible(self.BANNER)

    @allure.step('Assert that logo is displayed')
    def assert_that_logo_is_displayed(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)

    @allure.step('Assert contact center opening hours are displayed')
    def assert_contact_center_opening_hours_are_displayed(self):
        self.assertions.assert_that_element_is_visible(
            self.CONTACT_CENTER_OPENING_HOURS
        )

    @allure.step('Add to basket by index')
    def add_to_basket_by_index(self, i):
        time.sleep(1)
        self.get_element_by_index(self.BUTTON_ADD_TO_BASKET, i).click()

    @allure.step('Add product to favorites by index')
    def add_product_to_favorites_by_index(self, i):
        product = self.get_element_by_index(self.BUTTON_ADD_PRODUCT_TO_FAVORITES, i)
        product.click()

    @allure.step('Return text product by index')
    def get_text_product_by_index(self, i):
        product = self.get_element_by_index(self.BUTTON_ADD_TO_BASKET_PRODUCT_TEXT, i)
        return product.text

    @allure.step('Assert that product button has text in basket by index')
    def assert_that_product_button_has_text_in_basket_by_index(self, i):
        product = self.get_element_by_index(self.BUTTON_ADD_TO_BASKET, i)
        time.sleep(1)
        assert product.text == 'В корзине'

    @allure.step('Click bonus program')
    def click_bonus_program(self):
        self.click(self.BUTTON_BONUS_PROGRAM)

    @allure.step('Assert that bonus program baner is exist')
    def assert_that_bonus_program_baner_is_exist(self):
        self.assertions.assert_that_element_is_visible(
            self.BANNER_BONUS_PROGRAM
        )

    @allure.step('Click search headphones')
    def click_search_headphones(self):
        self.fill(self.SEARCH_FIELD, 'наушники')
        self.click_enter(self.SEARCH_FIELD)

    @allure.step('Assert that headphones are exist')
    def assert_that_headphones_are_exist(self):
        self.assertions.assert_that_element_is_visible(
            self.SEARCH_RESULT
        )

    @allure.step('Click partly pay')
    def click_partly_pay(self):
        self.click(self.BUTTON_PAYMENT_IN_PARTS)

    @allure.step('Assert partly payment banner is exist')
    def assert_partly_payment_banner_is_exist(self):
        self.assertions.assert_that_text_is_the_same(
            self.PAYMENT_IN_PARTS_BANNER,
            'Покупайте больше сейчас – платите частями'
        )

    @allure.step('Change city')
    def change_city(self, city):
        self.click(self.BUTTON_CHANGE_THE_CITY)
        time.sleep(1)
        self.click(self.BUTTON_CLEAR_FIELD_WITH_LOCATION)
        self.fill(self.FIELD_WITH_LOCATION, city)
        time.sleep(2)
        self.click_enter(self.FIELD_WITH_LOCATION)
        self.click(self.BUTTON_SAVE_NEW_CITY)

    @allure.step('Assert city on main page')
    def assert_city_on_main_page(self, city):
        self.assertions.assert_that_text_is_the_same(self.CITY, city)

    @allure.step('Click all promotions')
    def click_all_promotions(self):
        self.click(self.ALL_PROMOTIONS)

    @allure.step('Set filter value')
    def set_filter_value(self, sale_value):
        self.SALE_FILTER_VALUE = (By.XPATH, f'//span[text()="от {sale_value}%"]')

    @allure.step('Click apply sale filter')
    def click_apply_sale_filter(self):
        self.click(self.SALE_FILTER_VALUE)
        time.sleep(1)

    @allure.step('Assert sale vale of first product in filtered products')
    def assert_sale_vale_of_first_product_in_filtered_products(self, sale_value):
        sale = self.get_text(self.SALE_FIRST_GOOD)
        assert float(sale[1:-1]) >= sale_value

    @allure.step('Return count popular elements')
    def get_count_popular_elements(self):
        return len(self.driver.find_elements(*self.POPULAR_ELEMENT))

    @allure.step('Click show more popular elements')
    def click_show_more_popular_elements(self):
        self.click(self.BUTTON_SHOW_MORE)

    @allure.step('Click less than on popular products')
    def click_less_than_on_popular_products(self):
        self.click(self.BUTTON_CHEAPER_THAN_HUNDRED)

    @allure.step('Assert first froduct of populars is filtered')
    def assert_first_froduct_of_populars_is_filtered(self):
        time.sleep(1)
        first_el = self.get_element(self.POPULAR_ELEMENT)
        first_el_price = first_el.find_element(*self.ELEMENT_PRICE).text
        assert float(first_el_price.replace(',', '.')[:-3]) <= 100

    @allure.step('Click write to us')
    def click_write_to_us(self):
        self.click(self.WRITE_TO_US)

    @allure.step('Assert feedback window is exist')
    def assert_feedback_window_is_exist(self):
        self.assertions.assert_that_text_is_the_same(self.FEEDBACK_WINDOW, 'Обратная связь')

    @allure.step('Click input email in subscription form')
    def click_input_email_in_subscription_form(self):
        self.click(self.BUTTON_INPUT_EMAIL)

    @allure.step('Assert that email is not specified in subscription form')
    def assert_that_email_is_not_specified_in_subscription_form(self):
        self.assertions.assert_that_text_is_the_same(self.INPUT_ERROR_MESSAGE, 'Электронная почта не указана')

    @allure.step('Set email in subscription form')
    def set_email_in_subscription_form(self, email):
        self.fill(self.INPUT_EMAIL, email)

    @allure.step('Assert incorrect format email in subscription form')
    def assert_incorrect_format_email_in_subscription_form(self):
        self.assertions.assert_that_text_is_the_same(self.INPUT_ERROR_MESSAGE, 'Неправильный формат электронной почты')

    @allure.step('Assert that open account page')
    def assert_that_open_account_page(self):
        if self.check_element_is_exist(self.LOGIN_TO_ACCOUNT):
            self.assertions.assert_that_text_is_the_same(self.LOGIN_TO_ACCOUNT, 'Вход')
        else:
            self.assertions.assert_that_text_is_the_same(self.LOGIN_TO_ACCOUNT2, 'Вход')

    @allure.step('Click up button')
    def click_up_button(self):
        self.click(self.BUTTON_UP)

    @allure.step('Assert that now is window top')
    def assert_that_now_is_window_top(self):
        assert self.get_window_position() == 0

    @allure.step('Check button up')
    def check_button_up(self):
        self.scroll_to_bottom()
        self.click(self.BUTTON_UP)
        time.sleep(2)
        assert self.get_window_position() == 0
