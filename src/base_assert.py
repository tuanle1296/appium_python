from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Assert:
    def __int__(self, mobile_driver):
        self.mobile_driver = mobile_driver

    def verify_element_on_screen(self, element):
        try:
            self.mobile_driver.find_element(str(element[0]), str(element[1]))
        except NoSuchElementException:
            assert False, "Element " + str(element) + " is not on screen"

    def verify_element_not_on_screen(self, element):
        try:
            self.mobile_driver.find_element(str(element[0]), str(element[1]))
            assert False, "Element " + str(element) + " is displaying"
        except NoSuchElementException:
            pass

    @staticmethod
    def compare_string(text1, text2):
        assert text1 == text2, "Expected: " + str(text1) + " but: " + str(text2)


