from src.base import Common
from selenium.webdriver.common.by import By


class Clock(Common):
    current_title_screen = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/action_bar_title']")
    add_city_btn = (By.XPATH, "//android.widget.Button[@content-desc='Add city']")
    enter_city_field = (By.CLASS_NAME, "android.widget.EditText")
    first_suggestion = (By.XPATH, "//*[@class='android.support.v7.widget.RecyclerView']//*["
                                  "@class='android.widget.LinearLayout'][1]")
    current_city_time_zone = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/city_name' and "
                                        "contains(@text, 'text_to_replace')]")
    clock_tab = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/tab_menu_clock']")
    alarm_tab = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/tab_menu_alarm']")
    add_alarm_btn = (By.XPATH, "//android.widget.Button[@content-desc='Add alarm']")
    enable_keyboard_btn = (By.XPATH, "//android.widget.Button[@content-desc='Switch to text input mode for the time "
                                     "input.']")
    edit_hour = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_hour_text_input']")
    edit_minute = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_minute_text_input']")
    update_time_field = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_timepicker_edit_text']")
    set_AM_PM = (By.XPATH, "//com.google.android.material.button.MaterialButtonToggleGroup[@content-desc='Select AM "
                           "or PM']/android.widget.CompoundButton[contains(@text, 'text_to_replace')]")
    confirm_set_alarm = (By.XPATH, "//*[@resource-id='com.google.android.deskclock:id/material_timepicker_ok_button']")
    alarm_result = (By.XPATH, "//android.widget.TextView[contains(@content-desc, 'text_to_replace') and contains("
                              "@content-desc, 'another_text')]")

    def __int__(self, mobile_driver):
        super().__int__(mobile_driver)

    def verify_current_App_running_foreground_is_Clock(self):
        cur_app = self.get_current_foreground_app()
        self.compare_string(cur_app, "com.google.android.deskclock")

    def add_city(self, city_name):
        self.click_element(self.add_city_btn)
        self.input_text(self.enter_city_field, city_name)
        self.click_element(self.first_suggestion, 10)
        print("City name is: " + city_name)

    def verify_result_current_city_time_zone(self, city):
        self.wait(2)
        el = self.replace_text_in_element(self.current_city_time_zone, "text_to_replace", city)
        self.verify_element_on_screen(el)

    def navigate_to(self, element):
        el = getattr(self, element)
        self.click_element(el)

    def set_alarm(self, timer):
        print("Alarm set is: " + timer)
        timer_split = timer.split(":")
        self.click_element(self.add_alarm_btn)
        self.click_element(self.enable_keyboard_btn)
        self.click_element(self.edit_hour)
        self.input_text(self.update_time_field, timer_split[0])
        self.click_element(self.edit_minute)
        self.input_text(self.update_time_field, timer_split[1])
        el = self.replace_text_in_element(self.set_AM_PM, "text_to_replace", timer_split[1][-2:].upper())
        self.click_element(el)
        self.click_element(self.confirm_set_alarm)

    def verify_alarm_set(self, alarm):
        self.wait(2)
        el = self.replace_text_in_element(self.alarm_result, "text_to_replace", alarm[:-2])
        el = self.replace_text_in_element(el, "another_text", alarm[-2:].upper())
        self.verify_element_on_screen(el)
