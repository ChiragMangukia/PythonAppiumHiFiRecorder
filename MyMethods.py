from appium import webdriver


def invoke_app(lan, locale):
    desired_caps = {
        "build": "Python Android",
        "deviceName": "LMG710EM462f05f5", #Device Id
        "language": lan, #Langauge Code
        "locale": locale, #Country Code
        "appPackage": "com.lge.hifirecorder",
        "appActivity": "com.lge.hifirecorder.LaunchHifiRecorder",
        #"appPackage": "com.lge.filemanager",
        #"appActivity": "com.lge.filemanager.view.HomeActivity",
        #"appPackage": "com.android.settings",
        #"appActivity": "com.android.settings.Settings",
        "platformName": "Android",
        "autoGrantPermissions": "true"
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)