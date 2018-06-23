import MyMethods
import time
import selenium

driver = MyMethods.invoke_app("en", "in")

#Network Tab
#driver.find_element_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
#                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
#                             'android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TabHost/'
#                             'android.widget.TabWidget/android.widget.LinearLayout[1]').click()
time.sleep(2)

cou = driver.find_elements_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(className("android.widget.FrameLayout"))')
#aa = driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(className("android.widget.FrameLayout"))').text
#print(aa)
i = 0
for temp in cou:
    i = i + 1

print(i)

#Dual SIM Card
#driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.FrameLayout/"
#                             "android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()

#driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout").click()


def check_exist_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except selenium.common.exceptions.NoSuchElementException:
        return False
    return True


if check_exist_by_xpath('//android.widget.Button[@resource-id="android:id/button2"'):
    driver.find_element_by_xpath('//android.widget.Button[@resource-id="android:id/button2"').click()


if check_exist_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                             'android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TabHost/'
                             'android.widget.TabWidget/android.widget.LinearLayout[1]'):
    driver.find_element_by_xpath('//android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                             'android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'
                             'android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TabHost/'
                             'android.widget.TabWidget/android.widget.LinearLayout[1]').click()

print("Hello")