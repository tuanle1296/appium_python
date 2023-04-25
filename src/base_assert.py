from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Assert:
    def __int__(self, mobile_driver):
        self.mobile_driver = mobile_driver

    def verify_element_on_screen(self, element):
        try:
            WebDriverWait(self.mobile_driver, 2).until(EC.visibility_of_element_located(element))
        except:
            raise Exception(str(element) + " is not on page")

    def verify_element_not_on_screen(self, element):
        try:
            WebDriverWait(self.mobile_driver, 2).until(EC.invisibility_of_element_located(element))
        except:
            raise Exception(str(element) + " is on page")

    # def verify_text_on_screen(self, text):
    #     assert(text in self.mobile_driver.page_source, "No text found on page")

    @staticmethod
    def compare_string(text1, text2):
        if str(text1) != str(text2):
            raise Exception("Expected: " + str(text1) + " but: " + str(text2))


