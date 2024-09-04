from selenium.webdriver.common.by import By


class BasketPageLocators:
    BUTTON_BASKET = (By.CLASS_NAME, 'headerCart')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '[class="EmptyBasket_title__fTZV_ '
                                        'Title-module__title Title-module__h2"]')

    BUTTON_MAKE_ORDER = (By.XPATH, '//button[@data-testid="basketConfirmation"]')
    MAKE_ORDER_FIELD = (By.CSS_SELECTOR, '[class^="BasketCheckoutAuthScreen_header__2elDt"]')

    PROMO_CODE = (By.XPATH, '//input[@placeholder="Введите промокод"]')
    BUTTON_USE_PROMO_CODE = (By.XPATH, '//button[@data-testid="promocodeConfirmation"]')
    PROMO_CODE_IS_INVALID = (By.CLASS_NAME, 'ErrorMessage-module__message')

    BUTTON_PARTICIPATE_IN_PROMO_GAME = (By.XPATH, '//button[@data-testid="adgame-action"]')
    BUTTON_AGREE_WITH_PROMO_RULES = (By.CSS_SELECTOR, '[class="styles_checkbox__SEPT7"]')
    BUTTON_WANT_TO_PARTICIPATE = (By.CSS_SELECTOR, '[class~="AdModalContent_modalButton__Xe29Z"]')
    PROMOTIONAL_PRODUCT = (By.XPATH, '//p[@aria-label="Применённая акция"]')
    CANCEL_PROMO_GAME = (By.CSS_SELECTOR, '[class$="LinkButton-module__blue"]')
    CONFIRM_CANCEL_PROMO_GAME = (By.CSS_SELECTOR, '[class="Button-module__button '
                                                  'Button-module__pink-primary"]')

    PRODUCT_TEXT = (By.CSS_SELECTOR, '[class="BasketItem_title__MzCQ9"]')
    BUTTON_DELETE_PRODUCT = (By.CSS_SELECTOR, '[aria-label="Удалить товар"]')
    BUTTON_CONFIRM_DELETE_PRODUCT = (By.CSS_SELECTOR, '[class="Button-module__button '
                                                      'Button-module__pink-primary"]')
