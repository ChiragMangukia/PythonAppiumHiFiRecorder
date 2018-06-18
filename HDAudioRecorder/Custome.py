import MyMethods
import time

driver = MyMethods.invoke_app("en", "uk")


class Record:
    def my(self):
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                                     "android.view.ViewGroup/android.widget.ImageButton").click()
        time.sleep(2)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/"
                                     "android.support.v4.widget.DrawerLayout/android.widget.ListView/android.widget.LinearLayout[3]/"
                                     "android.widget.LinearLayout").click()
        time.sleep(2)

        global record_button
        record_button = driver.find_element_by_id('com.lge.hifirecorder:id/recordButtonLayout')

        driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                                     "android.widget.LinearLayout/android.widget.TextView[1]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                     "android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/"
                                     "android.widget.CheckedTextView[2]").click()
        time.sleep(3)

        record_button.click()
    #def record_voice(self):

        driver.find_element_by_id('com.lge.hifirecorder:id/stopButtonLayout').click()


temp=Record()
temp.my()
#temp.record_voice()

