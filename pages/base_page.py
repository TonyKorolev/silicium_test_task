from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidElementStateException


class BasePage:

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # For open url
    def open(self):
        self.browser.get(self.url)

    def is_element_visible(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_element_disabled(self, how, what):
        try:
            self.browser.find_element(how, what).get_attribute('disabled')
        except InvalidElementStateException:
            return False
        return True
