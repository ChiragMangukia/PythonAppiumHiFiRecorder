import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")

driver.find_element_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                             'android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TabHost/'
                             'android.widget.TabWidget/android.widget.LinearLayout[4]').click()
time.sleep(2)
driver.find_element_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                             'android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/android.support.v7.widget.RecyclerView/'
                             'android.widget.LinearLayout[2]').click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.RelativeLayout").click()
time.sleep(2)
driver.find_element_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/'
                             'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]')
time.sleep(3)
driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"HD Audio Recorder\"))").click()
time.sleep(1)
driver.find_element_by_xpath('//android.widget.TextView[@text="Permissions"]').click()
time.sleep(2)
status = driver.find_element_by_id('android:id/switch_widget').get_attribute("checked")
if status == "false":
    driver.find_element_by_id('android:id/switch_widget').click()

driver.press_keycode(4)