from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time
import os
from threading import Thread



caps =[
    {
    "deviceName": "Galaxy S20",
    "platformName": "Android",
    "platformVersion": "10",
    "app": "lt://APP1016043281710632734768779",  # Enter app_url here
    "isRealMobile": True,
    "build": "Parallel Native App automation",
    "name": "Samsung S20 Test",
    "network": False,
    "visual": True,
    "video": True
    },
    {
    "deviceName": "OnePlus 8",
    "platformName": "Android",
    "platformVersion": "11",
    "app": "lt://APP1016043281710632734768779",  # Enter app_url here
    "isRealMobile": True,
    "build": "Parallel Native App automation",
    "name": "OnePlus 8 Test",
    "network": False,
    "visual": True,
    "video": True
    },
    {
    "deviceName": "Pixel 6 Pro",
    "platformName": "Android",
    "platformVersion": "12",
    "app": "lt://APP1016043281710632734768779",  # Enter app_url here
    "isRealMobile": True,
    "build": "Parallel Native App automation",
    "name": "Pixel 6 Pro Test",
    "network": False,
    "visual": True,
    "video": True
    }
]


def run_session(desired_caps):
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = ""
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = ""
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@mobile-hub.lambdatest.com/wd/hub")
        
        colorElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/color")))
        colorElement.click()

        textElement = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((MobileBy.ID, "com.lambdatest.proverbial:id/Text")))
        textElement.click()

        toastElement = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/toast")))
        toastElement.click()

        notification = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/notification")))
        notification.click()

        geolocation = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/geoLocation")))
        geolocation.click()
        time.sleep(5)

        driver.back()

        home = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/buttonPage")))
        home.click()

        speedTest = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/speedTest")))
        speedTest.click()
        time.sleep(5)

        driver.back()

        browser = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/webview")))
        browser.click()

        url = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/url")))
        url.send_keys("https://www.lambdatest.com")

        find = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (MobileBy.ID, "com.lambdatest.proverbial:id/find")))
        find.click()
        driver.execute_script("lambda-status=passed")
        driver.quit()
    except:
        driver.execute_script("lambda-status=failed")
        driver.quit()

for cap in caps:
  Thread(target=run_session, args=(cap,)).start()