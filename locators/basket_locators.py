from selenium.webdriver.common.by import By


class BasketLocators:
    PRODUCT = (By.CSS_SELECTOR, '[class="BasketItem_topBlock__U4bk8"]')
    DELETE_PRODUCT_FROM_BASKET = (By.CSS_SELECTOR, '[class^="LinkButton-module__wrapper"][2]')
    ADD_PRODUCT_TO_FAVORITES = (By.CSS_SELECTOR, '[class^="LinkButton-module__wrapper"][3]')
    MAKE_AN_ORDER = (By.CSS_SELECTOR,'[class~="Button-module__pink-primary"][1]')
    SHIPPING_INFORMATION = (By.XPATH, '//*[@aria-label="delivery-info-block"]')
    INPUT_PROMOCODE = (By.XPATH, '//input[@name="promocode"]')
    PROMOCODE_CONFIRM = (By.XPATH, '//button[@data-testid="promocodeConfirmation"]')
    
