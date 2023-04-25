import allure
from datetime import datetime
from appium.webdriver.appium_service import AppiumService
from appium import webdriver


# base = Base()


def before_all(context):
    # base.execute_shell_file("shell/start_android_emulator.sh")
    context.dc = {
        'platformName': 'Android',
        'appPackage': 'com.google.android.deskclock',
        'udid': 'emulator-5554',
        'deviceName': 'Pixel 6 Pro',
        'automationName': 'UiAutomator2',
        # 'autoLaunch': 'false',
        'platformVersion': '13',
        'appActivity': 'com.android.deskclock.DeskClock'
    }

    context.service = AppiumService()

    """Launch appium server"""

    context.service.start(args=['-pa', '/wd/hub'])
    context.mobile_driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",
                                             desired_capabilities=context.dc)


def after_step(context, step):
    if step.status == 'failed':
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        allure.attach(context.mobile_driver.get_screenshot_as_png(),
                      name=dt_string + "_" + step.name,
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.mobile_driver.quit()
    context.service.stop()
    # base.execute_shell_file("shell/stop_android_emulator.sh")
