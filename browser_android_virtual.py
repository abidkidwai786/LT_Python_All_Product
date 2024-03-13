from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import os

desired_caps = {
    "deviceName": "Pixel 6",
    "platformName": "Android",
    "platformVersion": "13",
    "build": "Browser Automation Android Emulator",
    "name": "Sample Test - Python",
    "network": False,
    "visual": True,
    "video": True
}


def startingTest():

    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username here if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey here if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    try:
        driver = webdriver.Remote(desired_capabilities=desired_caps, command_executor="https://" +
                                  username+":"+accesskey+"@hub.lambdatest.com/wd/hub")

        driver.get("https://mfml.in/api/getInfo")
        colorElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "resolution")))
        colorElement.click()

        textElement = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "location")))
        textElement.click()

        toastElement = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "details")))
        toastElement.click()

        notification = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.ID, "timezone")))
        notification.click()

        time.sleep(5)
        driver.execute_script("lambda-status=passed")

        driver.quit()
    except:
        driver.execute_script("lambda-status=failed")
        driver.quit()


startingTest()