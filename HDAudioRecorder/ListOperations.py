from appium.webdriver.common.touch_action import TouchAction
import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")

class ListOperations:

    def open_list(self):
        driver.start_activity("com.lge.hifirecorder","com.lge.hifirecorder.VRListPlayActivity")

    def delete_using_longpress(self):
        recorded_file = driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                     "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/"
                                     "android.widget.ExpandableListView/android.widget.LinearLayout[1]")
        actions = TouchAction(driver)
        actions.long_press(recorded_file)
        actions.perform()
        delete_button = driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/"
                                        "android.widget.LinearLayout[1]")
        delete_button.click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                     "android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/"
                                     "android.widget.Button[1]").click()
        time.sleep(2)
        actions.long_press(recorded_file)
        actions.perform()
        time.sleep(2)
        delete_button.click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                    "android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/"
                                    "android.widget.Button[2]").click()

    def rename(self):
        recorded_file = driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                                "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/"
                                                "android.widget.ExpandableListView/android.widget.LinearLayout[1]")
        actions = TouchAction(driver)
        actions.long_press(recorded_file)
        actions.perform()
        rename_button = driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/"
                                                    "android.widget.LinearLayout[2]")
        rename_button.click()
        time.sleep(2)
        rename_editbox = driver.find_element_by_id('com.lge.hifirecorder:id/username_edit')
        rename_editbox.clear()
        rename_editbox.send_keys("Rename using Appium Automation")
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                     "android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/"
                                     "android.widget.Button[2]").click()

    def details(self):
        recorded_file = driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                                    "android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/"
                                                    "android.widget.ExpandableListView/android.widget.LinearLayout[1]")
        actions = TouchAction(driver)
        actions.long_press(recorded_file)
        actions.perform()
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/"
                                    "android.widget.LinearLayout[3]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                     "android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/"
                                     "android.widget.Button").click()

temp = ListOperations()
temp.open_list()
temp.delete_using_longpress()
temp.rename()
temp.details()