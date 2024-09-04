import time
from locators.favorites_locators import FavoritesPageLocators
from pages.base_page import BasePage
import allure


class FavoritesPage(BasePage, FavoritesPageLocators):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open favorites page')
    def open_favorites(self):
        time.sleep(1)
        self.click(self.BUTTON_FAVORITES)

    @allure.step('Assert that favorites is empty')
    def assert_that_favorites_is_empty(self):
        text = self.get_text(self.FAVORITES_ARE_EMPTY)
        self.assertions.assert_that_text_is_the_same(self.FAVORITES_ARE_EMPTY,
                                                     'Избранные товары\nНет избранных товаров')

    @allure.step('Assert that favorites is not empty')
    def assert_that_favorites_is_not_empty(self):
        self.assertions.assert_that_text_is_the_same(self.FAVORITES_ARE_EMPTY,
                                                     'Избранные товары')

    @allure.step('Return text from favorites by index')
    def get_text_from_favorites_by_index(self, i):
        return self.get_element_by_index(self.FAVORITES_PRODUCTS_TEXT, i).text

    @allure.step('Delete from favorites by index')
    def delete_from_favorites_by_index(self, i):
        self.get_element_by_index(self.BUTTON_DELETE_FROM_FAVORITES, i).click()
