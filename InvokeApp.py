from appium import webdriver
import time

desired_caps = {
    "build": "Python Android",
    "deviceName": "LMG710EM462f05f5",
    "appPackage": "com.lge.hifirecorder",
    "appActivity": "com.lge.hifirecorder.LaunchHifiRecorder",
    "platformName": "Android"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[@text='Custom']").click()
StartTime = driver.find_element_by_id('com.lge.hifirecorder:id/timer').text
print(StartTime)
driver.find_element_by_class_name('android.widget.Button').click()
driver.find_element_by_id('com.lge.hifirecorder:id/recordButtonLayout').click()
EndTime = driver.find_element_by_id('com.lge.hifirecorder:id/timer').text
print(EndTime)
#driver.find_element_by_xpath("//android.widget.FrameLayout[@resource-id='com.lge.hifirecorder:id/recordButtonLayout']").click()
#driver.find_element_by_class_name('android.widget.FrameLayout')[2].click()
#driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()
