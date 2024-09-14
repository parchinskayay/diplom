from pages.basket_page import BasketPage
from pages.main_page import MainPage
import time
import pytest
import allure


@allure.title('Basket is empty')
def test_basket_is_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    basket_page = BasketPage(driver)
    basket_page.open_basket()

    basket_page.assert_that_basket_is_empty()


@allure.title('Basket is not empty')
def test_basket_is_not_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()

    basket_page.assert_that_basket_is_not_empty()


@allure.title('Button make an order')
def test_assert_that_button_make_an_order_is_working(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.click_make_order()

    basket_page.assert_that_make_order_is_working()


@pytest.mark.parametrize("promocode", ['1111', '2222', '3333'])
@allure.title('Invalid promocode')
def test_assert_that_the_promo_code_is_invalid(driver, promocode):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.set_promocode(promocode)
    basket_page.click_use_promocode()

    basket_page.assert_that_promocode_is_incorrect()


@allure.title('Promotional product is visible')
def test_assert_that_promotional_product_is_visible(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.click_participate_in_promotional_game()

    basket_page.assert_that_promo_product_is_exist()


@allure.title('Cancel participation in promo game')
def test_assert_cancel_participation_in_promo_game(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.click_participate_in_promotional_game()
    basket_page.click_cancel_promotional_game()

    basket_page.assert_that_promo_product_does_not_exist()


@pytest.mark.parametrize("index", range(3))
@allure.title('The right product in the basket')
def test_add_product_in_basket_and_compare_names(driver, index):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    time.sleep(1)
    product_text = main_page.get_text_produduct_by_index(index)
    main_page.add_to_basket_by_index(index)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    product_text_from_basket = basket_page.get_product_text_by_index(0)

    assert product_text == product_text_from_basket


@pytest.mark.parametrize("n", [2, 4, 5])
@allure.title('The right products in the basket')
def test_add_some_products_in_basket_and_compare_names(driver, n):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    products_main_page_text = ''
    time.sleep(1)
    for i in range(n):
        products_main_page_text += main_page.get_text_produduct_by_index(i) + ' '
        main_page.add_to_basket_by_index(i)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    products_basket_text = ''
    for i in range(n):
        products_basket_text += basket_page.get_product_text_by_index(i) + ' '

    assert products_main_page_text == products_basket_text


@allure.title('Delete all products from basket')
def test_add_two_products_in_basket_and_delete_two_from_basket(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)
    main_page.add_to_basket_by_index(1)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.delete_from_basket_by_index(1)
    basket_page.delete_from_basket_by_index(0)

    basket_page.assert_that_basket_is_empty()


@allure.title('Delete not all products from basket')
def test_add_two_products_in_basket_and_delete_one_from_basket(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_to_basket_by_index(0)
    main_page.add_to_basket_by_index(1)

    basket_page = BasketPage(driver)
    basket_page.open_basket()
    basket_page.delete_from_basket_by_index(1)

    basket_page.assert_that_basket_is_not_empty()
