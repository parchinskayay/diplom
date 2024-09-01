from selenium.webdriver.common.by import By


class BasketPageLocators:
    BUTTON_BASKET = (By.CLASS_NAME, 'headerCart')
    FIRST_PRODUCT_IN_BASKET_WINDOW = (By.CLASS_NAME, 'BasketItem_item__WDRpK')

    FIRST_PRODUCT = (By.XPATH, '//*[@data-testid="card"][1]')
    BUTTON_FIRST_PRODUCT_ADD_TO_BASKET = (By.XPATH, '//button[@aria-label="Добавить в корзину"][1]')


