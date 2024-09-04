from pages.base_page import BasePage
from locators.basket_locators import BasketPageLocators
import time
import allure


class BasketPage(BasePage, BasketPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open basket page')
    def open_basket(self):
        time.sleep(1)
        self.click(self.BUTTON_BASKET)

    @allure.step('Assert that basket is empty')
    def assert_that_basket_is_empty(self):
        self.assertions.assert_that_text_is_the_same(self.BASKET_IS_EMPTY, 'Корзина пуста')

    @allure.step('Assert that basket is not empty')
    def assert_that_basket_is_not_empty(self):
        self.assertions.assert_that_element_doesnt_exist(self.BASKET_IS_EMPTY)

    @allure.step('Click make order')
    def click_make_order(self):
        time.sleep(1)
        self.click(self.BUTTON_MAKE_ORDER)

    @allure.step('Assert that make order is working')
    def assert_that_make_order_is_working(self):
        self.assertions.assert_that_text_is_the_same(self.MAKE_ORDER_FIELD, 'Оформление заказа')

    @allure.step('Set promocode')
    def set_promocode(self, promocode):
        self.fill(self.PROMO_CODE, promocode)

    @allure.step('Click use promocode')
    def click_use_promocode(self):
        time.sleep(1)
        self.click(self.BUTTON_USE_PROMO_CODE)

    @allure.step('Assert that promocode is incorrect')
    def assert_that_promocode_is_incorrect(self):
        self.assertions.assert_that_element_is_visible(self.PROMO_CODE_IS_INVALID)

    @allure.step('Click participate in promotional game')
    def click_participate_in_promotional_game(self):
        time.sleep(2)
        self.click(self.BUTTON_PARTICIPATE_IN_PROMO_GAME)
        self.click_mouse(self.BUTTON_AGREE_WITH_PROMO_RULES)
        self.click(self.BUTTON_WANT_TO_PARTICIPATE)

    @allure.step('Assert that promo product is exist')
    def assert_that_promo_product_is_exist(self):
        self.assertions.assert_that_text_is_the_same(self.PROMOTIONAL_PRODUCT, 'Суперцена')

    @allure.step('Click cancel promotional game')
    def click_cancel_promotional_game(self):
        time.sleep(1)
        self.click(self.CANCEL_PROMO_GAME)
        self.click(self.CONFIRM_CANCEL_PROMO_GAME)

    @allure.step('Assert that promo product does not exist')
    def assert_that_promo_product_does_not_exist(self):
        self.assertions.assert_that_element_doesnt_exist(self.PROMOTIONAL_PRODUCT)

    @allure.step('Return product text by index')
    def get_product_text_by_index(self, i):
        return self.get_element_by_index(self.PRODUCT_TEXT, i).text

    @allure.step('Delete from basket by index')
    def delete_from_basket_by_index(self, i):
        time.sleep(1)
        self.get_element_by_index(self.BUTTON_DELETE_PRODUCT, i).click()
        self.click(self.BUTTON_CONFIRM_DELETE_PRODUCT)
