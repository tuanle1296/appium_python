import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Common:
    def __init__(self, mobile_driver):
        self.mobile_driver = mobile_driver

    def get_current_foreground_app(self):
        return self.mobile_driver.current_package

    def click_element(self, element, timeout=5):
        try:
            WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located(element)).click()
        except:
            raise Exception("No element " + str(element) + " found")

    def input_text(self, element, text, timeout=5):
        try:
            el = WebDriverWait(self.mobile_driver, timeout).until(EC.visibility_of_element_located(element))
            el.click()
            el.clear()
            el.send_keys(text)
        except:
            raise Exception("No element " + str(element) + " found")

    @staticmethod
    def wait(timeout=5):
        time.sleep(timeout)

    @staticmethod
    def replace_text_in_element(element, old_string, new_string):
        string = element
        l = list(string)
        l[1] = l[1].replace(old_string, new_string)
        return tuple(l)

    def verify_element_on_screen(self, element):
        try:
            self.mobile_driver.find_element(str(element[0]), str(element[1]))
        except NoSuchElementException:
            assert False, "Element " + str(element) + " is not on screen"

    @staticmethod
    def compare_string(text1, text2):
        assert text1 == text2, "Expected: " + str(text1) + " but: " + str(text2)

