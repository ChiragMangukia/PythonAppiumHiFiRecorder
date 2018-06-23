import MyMethods
from appium.webdriver.common.touch_action import TouchAction
import time

driver = MyMethods.invoke_app("en", "uk")


class clock():
    def drag_drop(self):
        #driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
        #                             "android.widget.LinearLayout[2]/android.widget.TabHost/android.widget.HorizontalScrollView/"
        #                             "android.widget.FrameLayout/android.widget.TabWidget/android.widget.LinearLayout[1]").click()
        #time.sleep(2)
        driver.find_element_by_id("com.lge.clock:id/clock_fab").click()
        time.sleep(2)
        element_from = driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.ScrollView/"
                                                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                                    "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/"
                                                    "android.view.View/com.lge.clock.sui.SUIRadialTimePickerViewRuby$SUIRadialTimePickerTouchHelper[9]")
        element_to = element_from = driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                                                    "android.widget.LinearLayout/android.widget.ScrollView/"
                                                    "android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                                    "android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/"
                                                    "android.view.View/com.lge.clock.sui.SUIRadialTimePickerViewRuby$SUIRadialTimePickerTouchHelper[3]")
        actions = TouchAction(driver)
        actions.long_press(element_from).move_to(element_to).release().perform()


temp = clock()
temp.drag_drop()

