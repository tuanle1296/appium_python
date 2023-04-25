import subprocess
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Common:
    def __init__(self, mobile_driver):
        self.mobile_driver = mobile_driver

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

    # @staticmethod
    # def execute_shell_file(file_path):
    #     subprocess.call(['sh', file_path])
    #

    def wait_until_element_is_displayed(self, element, timeout=5):
        try:
            WebDriverWait(self.mobile_driver, timeout).until(
                EC.visibility_of_element_located(element)
            )
        except:
            raise Exception(str(element) + " is not found on page after " + str(timeout))

    @staticmethod
    def wait(timeout=5):
        time.sleep(timeout)

    def launch_mobile_app(self):
        self.mobile_driver.launch_app()

    def close_mobile_app(self):
        self.mobile_driver.close_app()

    def reset_mobile_app(self):
        self.mobile_driver.reset()

    def install_android_app(self, path_to_apk):
        self.mobile_driver.install_app(path_to_apk)

    def get_current_active_app(self):
        return self.mobile_driver.current_activity

    def get_text(self, element):
        return WebDriverWait(self.mobile_driver, 5).until(EC.visibility_of_element_located(element)).text
