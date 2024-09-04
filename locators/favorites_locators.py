from selenium.webdriver.common.by import By


class FavoritesPageLocators:
    BUTTON_FAVORITES = (By.XPATH, '//a[@href="/aside/"][1]')
    FAVORITES_ARE_EMPTY = (By.CSS_SELECTOR, '[class="FavoriteScreen_content__0dr4p"]')
    FAVORITES_PRODUCTS_TEXT = (By.CSS_SELECTOR, '[class="OldProductCard_name__q8eRK"]')
    BUTTON_DELETE_FROM_FAVORITES = (By.CSS_SELECTOR, '[class="OldProductCard_removeBtn__Comnc"]')
