from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from helpers.assertions import Assertions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

        self.assertions = Assertions(driver)

    def open_page(self, url):
        self.driver.get(url)

    def open_page_basket(self, selector):
        self.driver.get(self, *selector)

    def click(self, selector):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(selector)
        ).click()

    def click_enter(self, selector):
        self.get_element(selector).send_keys(Keys.ENTER)

    def fill(self, selector, text):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(selector)
        ).send_keys(text)

    def get_element(self, selector):
        return WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(selector))

    def wait_until_element_disappear(self, selector):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(selector)
        )

    def wait_for(self, selector, time_out=10):
        try:
            element = WebDriverWait(self.driver, time_out).until(
                EC.visibility_of_element_located(selector)
            )
            return element
        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {selector} does not find"

    def scroll_up_the_page(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def scroll_to_element(self, selector):
        element = self.driver.find_element(*selector)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
