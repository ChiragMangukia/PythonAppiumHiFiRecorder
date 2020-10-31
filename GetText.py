import MyMethods
import time

driver = MyMethods.invoke_app("hi", "in")

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
myText = driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                             "android.view.ViewGroup/android.widget.TextView").text
print(myText)