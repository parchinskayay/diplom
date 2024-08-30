from selenium.webdriver.common.by import By


class MainPageLocators:
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
    FIELD_WITH_LOCATION = (By.CSS_SELECTOR, '[class="select__input"]')
    BUTTON_CLEAR_FIELD_WITH_LOCATION = (By.CSS_SELECTOR, '[class="BaseSuggest-module__clearIndicator"]')
    BUTTON_SAVE_NEW_CITY = (By.XPATH, '//button[@class="Button-module__button '
                                      'style_baseActionButtonMargin__4haYC Button-module__blue-primary"]')

    BUTTON_FAVORITES_EMPTY = (By.CSS_SELECTOR, '[class="headerFavoritesBox headerCartBoxEmpty"]')
    BUTTON_FAVORITES = (By.CSS_SELECTOR, '[class="headerFavoritesBox"]')
    BUTTON_FIRST_PRODUCT_ADD_TO_FAVORITES = (By.XPATH, '//button[@aria-label="Добавить в избранное"][1]')

    REC = (By.CSS_SELECTOR, '[class="Recommendations_container__SX7F8"]')
    FIRST_FIELD_OF_REC = (By.XPATH, '//*[@data-testid="card"][1]')
    FIRST_FIELD_OF_REC_TEXT = (By.CSS_SELECTOR, '[class="CardInfo_info__cUeVj RecommendationProduct_info__fmq8N"]')
    FIRST_FIELD_OF_REC_BUTTON = (By.CSS_SELECTOR, '[class^="CardContainer_root__ziQTh"][1]')
    FAVORITES_FIRST_EL = (By.CSS_SELECTOR, '[class="OldProductCard_wrapper__rPxyQ"]')
    FAVORITES_FIRST_EL_TEXT = (By.CSS_SELECTOR, '[class="OldProductCard_name__q8eRK"]')

    BUTTON_DELETE_FROM_FAVORITES = (By.CSS_SELECTOR, '[class="OldProductCard_removeBtn__Comnc"]')

    BUTTON_BASKET_ON_MAIN_PAGE = (By.XPATH, '//*[@href="/order/?&checkTab=true"]')
    INFORMATION_THAT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '[class^="EmptyBasket_title__fTZV_"]')

    ALL_PROMOTIONS = (By.CSS_SELECTOR, '[class="styles_promoItem__aolWq"]')
    SALE_50 = (By.XPATH, '//*[text()="от 50%"]')
    SALE_FIRST_GOOD = (By.XPATH, '//*[@class="style_promoDiscount___y27J"][1]')

    BUTTON_SHOW_MORE = (By.CSS_SELECTOR, '[class="Button-module__button '
                                         'PopularsList_showMoreButton__KVZvm Button-module__blue-secondary"]')
    POPULAR_ELEMENT = (By.CSS_SELECTOR, '[class="EntitiesList_listItem__lgaHl PopularsList_entitylistListItem__NYS_A"]')

    BUTTON_CHEAPER_THAN_HUNDRED = (By.XPATH, '//span[text()="до 100 р."]')
    ELEMENT_PRICE = (By.CSS_SELECTOR, '[class="CardPrice_currentPrice__EU_7r ProductHome_priceCurrent__JHKhd"]')
