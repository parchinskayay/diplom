from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_WINDOW = (By.CSS_SELECTOR, '[class="AgreementCookie_modal__x3nra"]')
    BUTTON_REJECT_COOKIES = (By.CSS_SELECTOR, '[class="Button-module__button '
                                              'AgreementCookie_reject__f5oqP '
                                              'Button-module__gray-secondary"]')
    BUTTON_AGREE_COOKIES = (By.CSS_SELECTOR, '[class="Button-module__button '
                                             'Button-module__blue-primary"]')
    BUTTON_REJECT_COOKIES_SECOND = (By.CSS_SELECTOR, '[class="Button-module__button '
                                                     'Button-module__gray-secondary"]')

    DROPDOWN_WINDOW = (By.CSS_SELECTOR, '[class="popmechanic-content"]')
    BUTTON_CLOSE_DROPDOWN_WINDOW = (By.CSS_SELECTOR, '[class="popmechanic-submit popmechanic-submit-close"]')

    BANNER = (By.CSS_SELECTOR, '[class="Carousel_swiperContainer__uZrl1"]')
    LOGO = (By.XPATH, '//a[@class="logotypeImg"]')
    CONTACT_CENTER_OPENING_HOURS = (By.CSS_SELECTOR, '[class="styles_workingTimeText__2h7JO"]')

    BUTTON_ADD_TO_BASKET_PRODUCT_TEXT = (By.CSS_SELECTOR, '[class$="RecommendationProduct_info__fmq8N"]')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[aria-label="Добавить в корзину"]')

    BUTTON_BONUS_PROGRAM = (By.XPATH, '//a[@href="/special_offers/bonus.html"][1]')
    BANNER_BONUS_PROGRAM = (By.XPATH, '//img[@src="https://cdn21vek.by/img/tmp/656dc06b98ae0.jpeg"]')

    SEARCH_FIELD = (By.CSS_SELECTOR, '[class="Search_searchInput__RoV1W"]')
    SEARCH_RESULT = (By.CSS_SELECTOR, '[class="content__header cr-category_header"]')

    BUTTON_PAYMENT_IN_PARTS = (By.XPATH, '//a[@href="/special_offers/partly_pay.html"][1]')
    PAYMENT_IN_PARTS_BANNER = (By.XPATH, '//h1[@class="PartlyPay_header__ZVk0i"]')

    CITY = (By.CSS_SELECTOR, '[class="styles_localityBtn__qrGFQ"]')
    BUTTON_CHANGE_THE_CITY = (By.XPATH, '//button[@class="styles_localityBtn__qrGFQ"]')
    FIELD_WITH_LOCATION = (By.CSS_SELECTOR, '[class="select__input"]')
    BUTTON_CLEAR_FIELD_WITH_LOCATION = (By.CSS_SELECTOR, '[class="BaseSuggest-module__clearIndicator"]')
    BUTTON_SAVE_NEW_CITY = (By.XPATH, '//button[@class="Button-module__button '
                                      'style_baseActionButtonMargin__4haYC Button-module__blue-primary"]')

    BUTTON_ADD_PRODUCT_TO_FAVORITES = (By.CSS_SELECTOR, '[data-testid="card-favorites"]')

    ALL_PROMOTIONS = (By.CSS_SELECTOR, '[class="styles_promoItem__aolWq"]')
    SALE_FIRST_GOOD = (By.XPATH, '//*[@class="style_promoDiscount___y27J"][1]')

    BUTTON_SHOW_MORE = (By.CSS_SELECTOR, '[class="Button-module__button '
                                         'PopularsList_showMoreButton__KVZvm Button-module__blue-secondary"]')
    POPULAR_ELEMENT = (By.CSS_SELECTOR, '[class="EntitiesList_listItem__lgaHl PopularsList_entitylistListItem__NYS_A"]')

    BUTTON_CHEAPER_THAN_HUNDRED = (By.XPATH, '//span[text()="до 100 р."]')
    ELEMENT_PRICE = (By.CSS_SELECTOR, '[class="CardPrice_currentPrice__EU_7r ProductHome_priceCurrent__JHKhd"]')

    WRITE_TO_US = (By.CSS_SELECTOR, '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_feedback__eiVnQ"]')
    FEEDBACK_WINDOW = (By.CSS_SELECTOR, '[class="Form-module__formTitle"]')

    INPUT_EMAIL = (By.CSS_SELECTOR, '[class="style_inputStyle__ZKhdf"]')
    BUTTON_INPUT_EMAIL = (
    By.CSS_SELECTOR, '[class="SubscriptionForm_formWrapper__GiJED"] [class="SvgIcon-module__base"]')
    INPUT_ERROR_MESSAGE = (By.CSS_SELECTOR, '[class="input-error-message__message"]')
    LOGIN_TO_ACCOUNT = (By.CSS_SELECTOR, '[class="Form-module__formTitle"]')
    LOGIN_TO_ACCOUNT2 = (By.CSS_SELECTOR, '[class^="LoginFormNew_title__0zk9Q Text-module__text Text-module__large"]')

    BUTTON_UP = (By.CSS_SELECTOR, '[class="style_upButton__MUSza style_show__BRLkA"]')
