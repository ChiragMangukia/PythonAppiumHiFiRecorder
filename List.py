import MyMethods
import time

driver = MyMethods.invoke_app()

driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)
driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
time.sleep(1)

driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                             "android.widget.LinearLayout/android.widget.TextView").click()

#myCount = driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
#                            "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/"
#                            "android.widget.ExpandableListView/android.widget.LinearLayout/android.widget.LinearLayout").size()

myCount = driver.find_element_by_id('com.lge.hifirecorder:id/list_item_layout').click()
driver.find_element_by_id('com.lge.hifirecorder:id/closebutton').click()
driver.find_element_by_id('com.lge.hifirecorder:id/list_item_layout').click()
driver.find_element_by_id('com.lge.hifirecorder:id/playButton').click()
driver.find_element_by_id('com.lge.hifirecorder:id/playButton').click()
driver.find_element_by_id('com.lge.hifirecorder:id/deletelayout').click()
driver.find_element_by_id('android:id/button2').click()
driver.find_element_by_id('com.lge.hifirecorder:id/deletelayout').click()
driver.find_element_by_id('android:id/button1').click()