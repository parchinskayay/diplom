from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure

from helpers.assertions import Assertions


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.assertions = Assertions(driver)

    @allure.step('Open page')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Get element')
    def get_element(self, selector):
        try:
            return WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(selector)
            )

        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {selector} does not find"

    @allure.step('Get element by index')
    def get_element_by_index(self, selector, index):
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_any_elements_located(selector)
            )
            return elements[index]

        except (NoSuchElementException, TimeoutException, IndexError):
            assert False, f"Element {selector} by index {index} does not find"

    @allure.step('Click')
    def click(self, selector):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(selector)
            ).click()

        except (NoSuchElementException, TimeoutException):
            assert False, f"Element {selector} does not find"

    @allure.step('Click enter')
    def click_enter(self, selector):
        self.get_element(selector).send_keys(Keys.ENTER)

    @allure.step('Fill field with text')
    def fill(self, selector, text):
        self.get_element(selector).send_keys(text)

    @allure.step('Wait until element disappear')
    def wait_until_element_disappear(self, selector):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(selector)
        )

    @allure.step('Scroll to bottom')
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step('Get window position')
    def get_window_position(self):
        return self.driver.execute_script("return window.pageYOffset;")

    @allure.step('Scroll to element')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @staticmethod
    @allure.step('Get inner text')
    def get_inner_text(el):
        return el.get_attribute("innerText")

    @allure.step('Get text')
    def get_text(self, selector):
        return self.get_element(selector).text

    @allure.step('Check that element is exist')
    def check_element_is_exist(self, selector):
        return self.driver.find_elements(*selector)

    @allure.step('Click mouse')
    def click_mouse(self, selector):
        element = self.get_element(selector)
        actions = ActionChains(self.driver)
        actions.click(element).perform()
