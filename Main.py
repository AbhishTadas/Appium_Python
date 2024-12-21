import Emulator
import Server
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

Server.start_appium_server()  # provide port as argument if you wish to use port oter than 4732
Emulator.start_emulator("Mobile_33", "D:\\Android")
Emulator.wait_for_emulator_to_load()
time.sleep(10)

desired_caps = {
    'platformName': 'Android',  # Change to 'iOS' for iOS devices
    'platformVersion': '13.0',  # Change to your device's version
    'deviceName': 'Mobile_33',  # Change to your device's name
    'automationName': 'UiAutomator2'  # Use 'XCUITest' for iOS
}

capabilities_options = UiAutomator2Options().load_capabilities( desired_caps)
driver = webdriver.Remote(command_executor='http://localhost:4723', options=capabilities_options)
driver.implicitly_wait(20)
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Chrome"]').click()
# driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Close"]').click()
driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="Options for Discover"]').click()
driver.find_element(by=AppiumBy.XPATH,
                    value='//android.widget.TextView[@resource-id="com.android.chrome:id/menu_item_text" and '
                          '@text="Turn off"]').click()
