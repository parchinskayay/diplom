from selenium.webdriver.common.by import By


class HeadersLocators:
    COOKIE_WINDOW = (By.CSS_SELECTOR, '[class="AgreementCookie_modal__x3nra"]')
    BUTTON_AGREE_COOKIES = (By.CSS_SELECTOR, '[class="Button-module__button Button-module__blue-primary"]')

    DROPDOWN_WINDOW = (By.CSS_SELECTOR, '[class="popmechanic-content"]')
    BUTTON_CLOSE_DROPDOWN_WINDOW = (By.CSS_SELECTOR, '[class="popmechanic-submit popmechanic-submit-close"]')

    BANNER = (By.CSS_SELECTOR, '[class="Carousel_swiperContainer__uZrl1"]')
    LOGO = (By.XPATH, '//a[@class="logotypeImg"]')
    CONTACT_CENTER_OPENING_HOURS = (By.CSS_SELECTOR, '[class="styles_workingTimeText__2h7JO"]')

    FIRST_PRODUCT = (By.XPATH, '//div[@data-testid="image-container"][1]')
    BUTTON_FIRST_PRODUCT_ADD_TO_BASKET = (By.XPATH, '//*[@class="Button-module__buttonText"][1]')

    BUTTON_BONUS_PROGRAM = (By.XPATH, '//a[@href="/special_offers/bonus.html"][1]')
    BANNER_BONUS_PROGRAM = (By.XPATH, '//img[@src="https://cdn21vek.by/img/tmp/656dc06b98ae0.jpeg"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, '[class="Search_searchInput__RoV1W"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '[class="content__header cr-category_header"]')

    BUTTON_PAYMENT_IN_PARTS = (By.XPATH, '//a[@href="/special_offers/partly_pay.html"][1]')
    MONTHLY_PAYMENT = (By.CSS_SELECTOR, '[class="Calculator_priceBlock__3r472 Calculator_monthlyPayment__tfMOF"]')

    CITY = (By.CSS_SELECTOR, '[class="styles_localityBtn__qrGFQ"]')
    BUTTON_CHANGE_THE_CITY = (By.XPATH, '//button[@class="styles_localityBtn__qrGFQ"]')
    FIELD_WITH_LOCATION = (By.XPATH, '//input[@class="select__input"]')
    BUTTON_CLEAR_FIELD_WITH_LOCATION = (By.CSS_SELECTOR, '[class="BaseSuggest-module__clearIndicator"]')
    BUTTON_SAVE_NEW_CITY = (By.XPATH, '//button[@class="Button-module__button '
                                      'style_baseActionButtonMargin__4haYC Button-module__blue-primary"]')
