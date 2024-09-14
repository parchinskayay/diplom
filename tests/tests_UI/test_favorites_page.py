from pages.favorites_page import FavoritesPage
from pages.main_page import MainPage
import time
import pytest
import allure


@allure.title('Favorites are empty')
def test_favorites_are_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()

    favorites_page.assert_that_favorites_is_empty()


@allure.title('Favorites are not empty')
def test_favorites_are_not_empty(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_product_to_favorites_by_index(0)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()

    favorites_page.assert_that_favorites_is_not_empty()


@pytest.mark.parametrize("index", range(3))
@allure.title('The right product in the favorites')
def test_assert_text_added_to_favorites_product(driver, index):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    time.sleep(1)
    product_text = main_page.get_text_produduct_by_index(index)
    main_page.add_product_to_favorites_by_index(index)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    product_text_from_favorites = favorites_page.get_text_from_favorites_by_index(0)

    assert product_text == product_text_from_favorites


@pytest.mark.parametrize("n", [2, 3, 5])
@allure.title('Add some products to favorites')
def test_add_some_products_to_favorites_and_compare_names(driver, n):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    products_main_page_text = []

    for i in range(n):
        time.sleep(1)
        main_page.add_product_to_favorites_by_index(i)
        products_main_page_text.append(main_page.get_text_produduct_by_index(i))

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    products_favorites_text = []
    for i in range(n):
        products_favorites_text.append(favorites_page.get_text_from_favorites_by_index(i))

    products_main_page_text.sort()
    products_favorites_text.sort()

    assert products_main_page_text == products_favorites_text


@allure.title('Delete from favorites')
def test_add_to_favorites_and_delete_from_favorites(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_product_to_favorites_by_index(0)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    favorites_page.delete_from_favorites_by_index(0)

    favorites_page.assert_that_favorites_is_empty()


@allure.title('Delete all products from favorites')
def test_add_to_favorites_and_delete_from_favorites_two_products(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_product_to_favorites_by_index(0)
    main_page.add_product_to_favorites_by_index(1)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    favorites_page.delete_from_favorites_by_index(1)
    favorites_page.delete_from_favorites_by_index(0)

    favorites_page.assert_that_favorites_is_empty()


@allure.title('Delete not all products from favorites')
def test_add_to_favorites_two_products_and_delete_from_favorites_one_product(driver):
    main_page = MainPage(driver)
    main_page.open_page_and_reject_cookies()
    main_page.add_product_to_favorites_by_index(0)
    main_page.add_product_to_favorites_by_index(1)

    favorites_page = FavoritesPage(driver)
    favorites_page.open_favorites()
    favorites_page.delete_from_favorites_by_index(1)

    favorites_page.assert_that_favorites_is_not_empty()
