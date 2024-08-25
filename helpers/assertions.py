from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Assertions:

    def __init__(self, driver):
        self.driver = driver

    def assert_that_text_is_the_same(self, selector, text):
        el = self.driver.find_element(*selector)
        assert el.text == text

    def assert_that_element_is_visible(self, selector):
        assert self.driver.find_element(*selector)

    def assert_that_element_doesnt_exist(self, selector):
        assert not self.driver.find_elements(*selector)

    def assert_that_element_is_clickable(self, selector):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(selector)
        )

        assert self.driver.find_element(*selector)

    def assert_that_attribute_is_visible(self, selector, attribute, value):
        el = self.driver.find_element(*selector)
        assert el.get_attribute(attribute) == value

    def assert_that_attribute_class_is_visible(self, selector, value):
        self.assert_that_attribute_is_visible(*selector, 'class', value)

    def assert_that_element_contain_text(self, selector, value):
        element = self.driver.find_element(*selector)
        assert element.text == value, "Text from element, not the same"
