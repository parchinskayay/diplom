from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
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

    def fill(self, selector, text):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(selector)
        ).send_keys(text)

    def get_element(self, selector):
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(selector))

    def scroll_up_the_page(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def get_text(self, selector):
        element = self.get_element(selector)
        return element.text

    def select_by_index(self, selector, index):
        select = Select(self.get_element(selector))
        select.select_by_index(index)

    def select_by_visible_text(self, selector, text):
        select = Select(self.get_element(selector))
        select.select_by_visible_text(text)

    def select_by_value(self, selector, value):
        select = Select(self.get_element(selector))
        select.select_by_value(value)

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def prompt(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def open_new_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_current_window(self):
        return self.driver.current_window_handle

    def open_empty_window(self):
        return self.driver.execute_script("window.open()")

    def switch_to_frame(self, selector):
        el = self.get_element(selector)
        self.driver.switch_to.frame(el)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def upload_file(self, selector, path):
        el = self.get_element(selector)
        el.send_keys(path)
        submit = self.get_element((By.CSS_SELECTOR, '[type="submit"]'))
        submit.submit()
