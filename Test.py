import MyMethods
import time
import os

driver = MyMethods.invoke_app()

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_class_name('android.widget.ImageButton').click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[@text='Custom']").click()
StartTime = driver.find_element_by_id('com.lge.hifirecorder:id/timer').text
print(StartTime)
driver.orientation = "LANDSCAPE"
driver.find_element_by_class_name('android.widget.Button').click()
#driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
#                             "android.support.v4.widget.DrawerLayout/android.widget.LinearLayout/"
 #                            "android.widget.LinearLayout[2]/android.widget.LinearLayout/"
  #                           "android.widget.FrameLayout[2]").click()


#driver.find_element_by_class_name('android.widget.Button').click()
driver.find_element_by_id('com.lge.hifirecorder:id/recordButtonLayout').click()
EndTime = driver.find_element_by_id('com.lge.hifirecorder:id/timer').text
print(EndTime)
time.sleep(2)
driver.find_element_by_id('com.lge.hifirecorder:id/stopButtonLayout').click()
driver.orientation = "PORTRAIT"
time.sleep(2)
driver.save_screenshot(os.getcwd() + '/myscreenshot.png')