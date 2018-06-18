import selenium
import MyMethods
import time


driver = MyMethods.invoke_app("en", "in")

def check_exist_by_id(id):
    try:
        driver.find_element_by_id(id)
    except selenium.common.exceptions.NoSuchElementException:
        return False
    return True

if check_exist_by_id('com.lge.eula:id/btn_agree'):
    driver.find_element_by_id('com.lge.eula:id/btn_agree').click()

time.sleep(2)

#driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
#time.sleep(1)
#driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
#time.sleep(1)

if check_exist_by_id('com.lge.hifirecorder:id/tip_help_next_button'):
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_next_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_previous_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_next_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_next_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_next_button').click()
    time.sleep(1)
    driver.find_element_by_id('com.lge.hifirecorder:id/tip_help_next_button').click()
    time.sleep(1)

driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                             "android.widget.LinearLayout/android.widget.TextView").click()

#cou = driver.find_elements_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(className("android.widget.FrameLayout"))')

if check_exist_by_id('com.lge.hifirecorder:id/list_item_layout'):
    driver.find_element_by_id('com.lge.hifirecorder:id/list_item_layout').click()
    driver.find_element_by_id('com.lge.hifirecorder:id/closebutton').click()
    driver.find_element_by_id('com.lge.hifirecorder:id/list_item_layout').click()
    driver.find_element_by_id('com.lge.hifirecorder:id/playButton').click()
    if check_exist_by_id('com.lge.hifirecorder:id/playButton'):
        driver.find_element_by_id('com.lge.hifirecorder:id/playButton').click()
        driver.find_element_by_id('com.lge.hifirecorder:id/deletelayout').click()
        driver.find_element_by_id('android:id/button2').click()
        driver.find_element_by_id('com.lge.hifirecorder:id/deletelayout').click()
        driver.find_element_by_id('android:id/button1').click()

driver.find_element_by_xpath("//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/"
                             "android.widget.LinearLayout/android.widget.TextView").click()

def record_voice(duration):
    driver.find_element_by_id('com.lge.hifirecorder:id/recordButtonLayout').click()
    time.sleep(int(duration))
    driver.find_element_by_id('com.lge.hifirecorder:id/stopButtonLayout').click()


record_voice(5)