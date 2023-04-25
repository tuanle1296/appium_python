from src.base import Common
from src.base_assert import Assert
from selenium.webdriver.common.by import By


class Locators:
    text_to_replace = ""
    current_title_screen = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/action_bar_title']")
    add_city_btn = (By.XPATH, "//android.widget.Button[@content-desc='Add city']")
    enter_city_field = (By.CLASS_NAME, "android.widget.EditText")
    first_suggestion = (By.XPATH, "//*[@class='android.support.v7.widget.RecyclerView']//*["
                                  "@class='android.widget.LinearLayout'][1]")
    current_city_time_zone = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/city_name' and "
                                               "contains(@text, '{0}')]".format(text_to_replace))
    clock_tab = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/tab_menu_clock']")
    alarm_tab = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/tab_menu_alarm']")
    add_alarm_btn = (By.XPATH, "//android.widget.Button[@content-desc='Add alarm']")
    enable_keyboard_btn = (By.XPATH, "//android.widget.Button[@content-desc='Switch to text input mode for the time input.']")
    edit_hour = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_hour_text_input']")
    edit_minute = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_minute_text_input']")
    update_time_field = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_timepicker_edit_text']")
    set_AM_PM = (By.XPATH, "//com.google.android.material.button.MaterialButtonToggleGroup[@content-desc='Select AM "
                           "or PM']/android.widget.CompoundButton[contains(@text, '{0}')]".format(text_to_replace))
    confirm_set_alarm = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_timepicker_ok_button']")
    alarm_result = (By.XPATH, "//android.widget.TextView[contains(@content-desc, '{0}')]".format(text_to_replace))


class Clock(Common, Assert):

    def __int__(self, mobile_driver):
        self.mobile_driver = mobile_driver

    def verify_that(self, arg, text):
        el = getattr(Locators, arg)
        cur_text = self.get_text(el)
        self.compare_string(cur_text, text)

    def add_city(self, city_name):
        locators = Locators
        self.click_element(locators.add_city_btn)
        self.input_text(locators.enter_city_field, city_name)
        self.click_element(locators.first_suggestion, 10)

    def verify_result_current_city_time_zone(self, city):
        locators = Locators
        self.wait(2)
        locators.text_to_replace = city
        self.verify_element_on_screen(locators.current_city_time_zone)

    def click_on(self, element):
        el = getattr(Locators, element)
        self.click_element(el)

    def set_alarm(self, timer):
        locators = Locators
        timer_split = timer.split(":")
        self.click_element(locators.add_alarm_btn)
        self.click_element(locators.enable_keyboard_btn)
        self.click_element(locators.edit_hour)
        self.input_text(locators.update_time_field, timer_split[0])
        self.click_element(locators.edit_minute)
        self.input_text(locators.update_time_field, timer_split[1])
        locators.text_to_replace = timer_split[1][-2:]
        self.click_element(locators.set_AM_PM)
        self.click_element(locators.confirm_set_alarm)

    def verify_alarm_set(self, alarm):
        locators = Locators
        self.wait(2)
        locators.text_to_replace = alarm
        self.verify_element_on_screen(locators.alarm_result)



