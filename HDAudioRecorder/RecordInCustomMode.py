import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")


class Record:
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                                 "android.view.ViewGroup/android.widget.ImageButton").click()
    time.sleep(2)
    driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                 "android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.LinearLayout[2]/"
                                 "android.widget.LinearLayout").click()
    time.sleep(2)

    def record_voice(self):
        driver.find_element_by_id('com.lge.hifirecorder:id/recordButtonLayout').click()
        time.sleep(1)
        driver.find_element_by_id('com.lge.hifirecorder:id/stopButtonLayout').click()


temp=Record()
temp.record_voice()

