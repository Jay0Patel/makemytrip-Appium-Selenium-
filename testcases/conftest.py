import pytest as pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
import os



@pytest.fixture(scope = "class")
def setup(request):
    desired_capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "appPackage": "com.makemytrip",
        "appActivity": "com.mmt.travel.app.home.ui.SplashActivity"
        # "noReset": True,
        # "fullReset":False
    }


    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.quit()


