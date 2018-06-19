import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")

driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                                     "android.view.ViewGroup/android.widget.ImageButton").click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                     "android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.LinearLayout[3]/"
                                     "android.widget.LinearLayout").click()
time.sleep(2)

driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                             "android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageButton").click()

driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/"
                             "android.widget.LinearLayout[3]").click()

class SettingsOperations:

    def open_settings_normal_mode(self):
        