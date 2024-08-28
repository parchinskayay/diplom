import time

from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage


class MainPage(BasePage, HeadersLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def assert_agree_cookies(self):
        self.assertions.assert_that_element_is_visible(self.COOKIE_WINDOW)
        self.click(self.BUTTON_AGREE_COOKIES)
        self.wait_until_element_disappear(self.COOKIE_WINDOW)
        self.assertions.assert_that_element_doesnt_exist(self.COOKIE_WINDOW)

    def click_agree_cookies(self):
        self.wait_for(self.COOKIE_WINDOW)
        self.click(self.BUTTON_AGREE_COOKIES)

    def close_dropdown_window_about_sales(self):
        self.wait_for(self.DROPDOWN_WINDOW)
        self.assertions.assert_that_element_is_visible(self.DROPDOWN_WINDOW)
        self.assertions.assert_that_element_is_visible(self.BUTTON_CLOSE_DROPDOWN_WINDOW)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_CLOSE_DROPDOWN_WINDOW)
        self.click(self.BUTTON_CLOSE_DROPDOWN_WINDOW)
        self.wait_until_element_disappear(self.DROPDOWN_WINDOW)
        self.assertions.assert_that_element_doesnt_exist(self.DROPDOWN_WINDOW)

    def assert_that_banner_is_displayed(self):
        self.assertions.assert_that_element_is_visible(self.BANNER)

    def assert_that_logo_is_displayed(self):
        self.assertions.assert_that_element_is_visible(self.LOGO)

    def contact_center_opening_hours(self):
        self.assertions.assert_that_element_is_visible(self.CONTACT_CENTER_OPENING_HOURS)

    def choose_the_first_product_and_add_to_basket(self):
        self.assertions.assert_that_element_is_visible(self.FIRST_PRODUCT)
        self.assertions.assert_that_element_is_clickable(self.BUTTON_FIRST_PRODUCT_ADD_TO_BASKET)
        self.click(self.BUTTON_FIRST_PRODUCT_ADD_TO_BASKET)
        time.sleep(2)
        self.assertions.assert_that_text_is_the_same(self.BUTTON_FIRST_PRODUCT_ADD_TO_BASKET, 'В корзине')

    def bonus_program_button_is_working(self):
        self.assertions.assert_that_element_is_visible(self.BUTTON_BONUS_PROGRAM)
        self.click(self.BUTTON_BONUS_PROGRAM)
        self.assertions.assert_that_element_is_visible(self.BANNER_BONUS_PROGRAM)

    def search_field_is_working(self):
        self.assertions.assert_that_element_is_visible(self.SEARCH_FIELD)
        self.fill(self.SEARCH_FIELD, 'наушники')
        self.click_enter(self.SEARCH_FIELD)
        self.assertions.assert_that_element_is_visible(self.SEARCH_RESULT)

    def button_payment_in_parts_is_working(self):
        self.click(self.BUTTON_PAYMENT_IN_PARTS)
        self.scroll_to_element(self.MONTHLY_PAYMENT)
        self.assertions.assert_that_element_is_visible(self.MONTHLY_PAYMENT)

    def change_city(self):
        self.assertions.assert_that_element_is_visible(self.CITY)
        self.click(self.BUTTON_CHANGE_THE_CITY)
        self.click(self.BUTTON_CLEAR_FIELD_WITH_LOCATION)
        self.fill(self.FIELD_WITH_LOCATION, 'г. Брест')
        time.sleep(2)
        self.click_enter(self.FIELD_WITH_LOCATION)
        time.sleep(2)
        self.click(self.BUTTON_SAVE_NEW_CITY)
        time.sleep(2)
        self.assertions.assert_that_text_is_the_same(self.CITY, 'г. Брест')
