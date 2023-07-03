
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import pyperclip

desired_cap = {
    "deviceName": "RZ8N915EZPJ",
    "platformName": "Android",
    "appPackage": "com.makemytrip",
    "appActivity": "com.mmt.travel.app.home.ui.SplashActivity"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Language selection
Continue_button = driver.find_element(AppiumBy.ID, "com.makemytrip:id/continueButton")
Continue_button.click()
time.sleep(2)
# Email Id
None_of_above_button = driver.find_element(AppiumBy.ID, "com.google.android.gms:id/cancel")
None_of_above_button.click()
time.sleep(2)
email_id_type = driver.find_element(AppiumBy.ID, "com.makemytrip:id/inputFieldChild").send_keys("json7753@gmail.com")
time.sleep(2)
Continue_button_2 = driver.find_element(AppiumBy.ID, "com.makemytrip:id/btn_continue")
Continue_button_2.click()
time.sleep(2)

# Start the gmail app
driver.start_activity('com.google.android.gm', 'com.google.android.gm.ConversationListActivityGmail')
time.sleep(3)

driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='OTP to create your MakeMyTrip account']").click()
time.sleep(2)
OTP = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.GridView/android.view.View[1]/android.view.View/android.view.View/android.widget.TextView[1]')
split_text = OTP.text.split('OTP is')[-1]
# print(split_text)
# starting_parts = OTP.split('OTP is')[-1]
copy_code = pyperclip.copy(split_text)
time.sleep(3)

# Switch app to makemytrip
driver.activate_app("com.makemytrip")
time.sleep(2)
copy_code_1 = pyperclip.paste()
# Paste code
time.sleep(3)
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys(copy_code_1)
Continue_button_3 = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Button")
Continue_button_3.click()
