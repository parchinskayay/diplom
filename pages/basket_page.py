from pages.base_page import BasePage
from locators.basket_locators import BasketPageLocators


class BasketPage(BasePage, BasketPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def button_open_basket(self):
        self.click(self.BUTTON_BASKET)

    def basket_is_empty(self):
        self.assertions.assert_that_element_is_clickable(self.BUTTON_BASKET)
        self.assertions.assert_that_element_doesnt_exist(self.FIRST_PRODUCT_IN_BASKET_WINDOW)

    def check_add_product_to_basket(self):
        self.assertions.assert_that_element_is_visible(self.FIRST_PRODUCT)
        self.click(self.BUTTON_FIRST_PRODUCT_ADD_TO_BASKET)
        self.click(self.BUTTON_BASKET)
        self.assertions.assert_that_element_is_visible(self.FIRST_PRODUCT_IN_BASKET_WINDOW)
