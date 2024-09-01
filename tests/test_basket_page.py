from pages.basket_page import BasketPage
from test_main_page import init_main_page


def test_basket_is_empty(driver):
    init_main_page(driver)

    basket_page = BasketPage(driver)
    basket_page.basket_is_empty()


def test_check_add_product_to_basket(driver):
    init_main_page(driver)

    basket_page = BasketPage(driver)
    basket_page.check_add_product_to_basket()
