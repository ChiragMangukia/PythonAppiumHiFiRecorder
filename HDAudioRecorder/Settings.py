import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")


class SettingsOperations:

    def open_normal_mode(self):
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                                     "android.view.ViewGroup/android.widget.ImageButton").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                     "android.support.v4.widget.DrawerLayout/android.widget.ListView/"
                                     "android.widget.LinearLayout[1]/android.widget.LinearLayout").click()
        time.sleep(2)

    def open_settings_normal_mode(self):
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                                     "android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageButton").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/"
                                     "android.widget.LinearLayout[3]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                     "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/"
                                     "android.widget.FrameLayout/android.widget.LinearLayout").click()

temp = SettingsOperations()
temp.open_normal_mode()
temp.open_settings_normal_mode()


