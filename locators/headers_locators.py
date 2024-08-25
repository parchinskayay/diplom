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

    BONUS_PROGRAM = (By.XPATH, '//li[@class="styles_navMenuItem__5EPNe"]')
    SEARCH = (By.XPATH, '//input[@aria-label ="search"]')
    CATALOG_BUTTON = (By.XPATH, '//button[@class="styles_catalogButton__z9L_j"]')
    ACCOUNT = (By.XPATH, '//input[@class="styles_userToolsToggler__c2aHe"]')
    CITY = (By.CSS_SELECTOR, '[class="styles_localityBtn__qrGFQ"]')
    CONTACTS_BUTTON = (By.XPATH, '//button[@class="styles_headerTitle__OyXGt styles_active__2Ygqn"]')
    WORKING_TIME = (By.CSS_SELECTOR, '[class="styles_workingTimeText__2h7JO"]')
    ALL_SALES = (By.CSS_SELECTOR, '[class="styles_fixed__RU8zI"]')

    BASKET = (By.CSS_SELECTOR, '[class="headerCartBox"]')
