from helpers.url import BASE_URL
from locators.headers_locators import HeadersLocators
from pages.base_page import BasePage


class HeadersElements(BasePage, HeadersLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.open_page(BASE_URL)

    def click_agree_cookies(self):
        self.open()
        if self.get_element(self.COOKIE_WINDOW):
            self.click(self.AGREE_COOKIES)

    def close_dropdown_window_about_sales(self):
        self.open()
        self.click_agree_cookies()
        self.click(self.CLOSE_DROPDOWN_WINDOW)

    def assert_that_banner_is_displayed(self):
        self.click_agree_cookies()
        self.assertions.assert_that_element_is_visible(self.BANNER)

    def assert_that_logo_is_displayed(self):
        self.click_agree_cookies()
        self.assertions.assert_that_element_is_visible(self.LOGO)

    def choose_the_first_product_and_add_to_basket(self):
        self.open()
        self.click_agree_cookies()
        self.get_element(self.FIRST_PRODUCT)
        self.click(self.FIRST_PRODUCT_ADD_TO_BASKET)
        self.scroll_up_the_page()
        self.get_element(self.BASKET).click()

    def contact_center_opening_hours(self):
        self.click_agree_cookies()
        self.assertions.assert_that_element_is_visible(self.СONTACT_CENTER_OPENING_HOURS)
