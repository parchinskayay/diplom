import time
from helpers.url import BASE_URL
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage, MainPageLocators):

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
        time.sleep(5)
        self.assertions.assert_that_element_is_visible(self.SEARCH_RESULT)

    def button_payment_in_parts_is_working(self):
        self.click(self.BUTTON_PAYMENT_IN_PARTS)
        self.scroll_to_element(self.MONTHLY_PAYMENT)
        self.assertions.assert_that_element_is_visible(self.MONTHLY_PAYMENT)

    def change_city(self):
        self.assertions.assert_that_element_is_visible(self.CITY)
        self.click(self.BUTTON_CHANGE_THE_CITY)
        time.sleep(5)
        self.click(self.BUTTON_CLEAR_FIELD_WITH_LOCATION)
        time.sleep(2)
        self.fill(self.FIELD_WITH_LOCATION, 'г. Брест')
        time.sleep(5)
        self.click_enter(self.FIELD_WITH_LOCATION)
        self.click(self.BUTTON_SAVE_NEW_CITY)
        time.sleep(2)
        self.assertions.assert_that_text_is_the_same(self.CITY, 'г. Брест')

    def favorites_is_empty(self):
        self.click(self.BUTTON_FAVORITES_EMPTY)
        self.assertions.assert_that_element_doesnt_exist(self.BUTTON_DELETE_FROM_FAVORITES)

    def favorites_is_not_empty(self):
        self.click(self.BUTTON_FIRST_PRODUCT_ADD_TO_FAVORITES)
        self.click(self.BUTTON_FAVORITES)
        self.assertions.assert_that_element_is_visible(self.BUTTON_DELETE_FROM_FAVORITES)

    def basket_is_empty(self):
        self.click(self.BUTTON_BASKET_ON_MAIN_PAGE)
        self.assertions.assert_that_element_is_visible(self.INFORMATION_THAT_BASKET_IS_EMPTY)

    def basket_is_not_empty(self):
        self.click(self.BUTTON_FIRST_PRODUCT_ADD_TO_BASKET)
        self.click(self.BUTTON_BASKET_ON_MAIN_PAGE)
        time.sleep(2)
        self.assertions.assert_that_element_doesnt_exist(self.INFORMATION_THAT_BASKET_IS_EMPTY)

    def favorites_are_working(self):
        recommendation = self.get_element(self.REC)
        first_el = recommendation.find_element(*self.FIRST_FIELD_OF_REC)
        first_el_text_el = first_el.find_element(*self.FIRST_FIELD_OF_REC_TEXT)
        first_el_text = self.get_inner_text(first_el_text_el)
        first_el_button_favorites = first_el.find_element(*self.BUTTON_FIRST_PRODUCT_ADD_TO_FAVORITES)
        first_el_button_favorites.click()
        self.click(self.BUTTON_FAVORITES)
        fav_first_el = self.get_element(self.FAVORITES_FIRST_EL)
        fav_first_el_text = fav_first_el.find_element(*self.FAVORITES_FIRST_EL_TEXT).text
        assert first_el_text == fav_first_el_text

    def delete_from_favorites(self):
        recommendation = self.get_element(self.REC)
        first_el = recommendation.find_element(*self.FIRST_FIELD_OF_REC)
        first_el_button_favorites = first_el.find_element(*self.BUTTON_FIRST_PRODUCT_ADD_TO_FAVORITES)
        first_el_button_favorites.click()
        self.click(self.BUTTON_FAVORITES)
        self.wait_for(self.BUTTON_DELETE_FROM_FAVORITES)
        self.click(self.BUTTON_DELETE_FROM_FAVORITES)
        self.assertions.assert_that_element_doesnt_exist(self.FAVORITES_FIRST_EL)

    def check_sale_filter(self):
        self.click(self.ALL_PROMOTIONS)
        self.click(self.SALE_50)
        time.sleep(2)
        sale = self.get_text(self.SALE_FIRST_GOOD)
        assert float(sale[1:-1]) >= 50

    def assert_show_more_button(self):
        count_popular_els_old = len(self.driver.find_elements(*self.POPULAR_ELEMENT))
        self.click(self.BUTTON_SHOW_MORE)
        count_popular_els_new = len(self.driver.find_elements(*self.POPULAR_ELEMENT))
        assert count_popular_els_old < count_popular_els_new

    def check_popular_filter_cheap(self):
        self.click(self.BUTTON_CHEAPER_THAN_HUNDRED)
        time.sleep(2)
        first_el = self.get_element(self.POPULAR_ELEMENT)
        first_el_price = first_el.find_element(*self.ELEMENT_PRICE).text
        assert float(first_el_price.replace(',', '.')[:-3]) <= 100

    def check_write_to_us_button(self):
        self.wait_for(self.WRITE_TO_US)
        self.click(self.WRITE_TO_US)
        self.wait_for(self.FEEDBACK_WINDOW)
        self.assertions.assert_that_text_is_the_same(self.FEEDBACK_WINDOW, 'Обратная связь')

    def check_subscription_form_empty(self):
        self.wait_for(self.INPUT_EMAIL)
        self.click(self.BUTTON_INPUT_EMAIL)
        self.assertions.assert_that_text_is_the_same(self.INPUT_ERROR_MESSAGE, 'Электронная почта не указана')

    def check_subscription_form_incorrect_email(self):
        self.wait_for(self.INPUT_EMAIL)
        self.fill(self.INPUT_EMAIL, '1111')
        self.click(self.BUTTON_INPUT_EMAIL)
        self.assertions.assert_that_text_is_the_same(self.INPUT_ERROR_MESSAGE, 'Неправильный формат электронной почты')

    def check_subscription_form_work_correct(self):
        self.wait_for(self.INPUT_EMAIL)
        self.fill(self.INPUT_EMAIL, 'example@example.com')
        self.click(self.BUTTON_INPUT_EMAIL)
        time.sleep(2)
        if self.check_element_is_exist(self.LOGIN_TO_ACCOUNT):
            self.assertions.assert_that_text_is_the_same(self.LOGIN_TO_ACCOUNT, 'Вход')
        else:
            self.assertions.assert_that_text_is_the_same(self.LOGIN_TO_ACCOUNT2, 'Вход')

    def check_button_up(self):
        self.scroll_to_bottom()
        self.click(self.BUTTON_UP)
        time.sleep(2)
        assert self.get_window_position() == 0
