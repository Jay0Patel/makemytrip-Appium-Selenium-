import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip


class LaunchPage():
    def __init__(self, driver):
        self.driver = driver

    def language_selection(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.makemytrip:id/continueButton"))).click()

    def sign_up(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.gms:id/cancel"))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.makemytrip:id/inputFieldChild"))).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, "com.makemytrip:id/btn_continue"))).click()

    def gmail_OTP(self):
        time.sleep(5)
        self.driver.background_app(-1)
        self.driver.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
        OTP_line = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[4]")))
        text = OTP_line.text.split('OTP is ')[-1]
        number = text.split(' ')[0].strip()
        pyperclip.copy(number)
        self.OTP_pass = pyperclip.paste()

    def OTP(self):
        self.driver.activate_app('com.makemytrip')
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))).send_keys(self.OTP_pass)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.Button"))).click()
        time.sleep(10)

    def details(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, ""))).send_keys("jay")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, ""))).send_keys("")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, ""))).send_keys("")

