from appium import webdriver
import os
import time
from appium.webdriver.common.appiumby import AppiumBy

def getCaps():
    desired_caps = {
        "deviceName" : "Apple TV",
        "platformVersion" :  "16",
        "platform" : "tvos",
        "isRealMobile":True,
        "build": "Apple TV Testing",
        "video": True,
        "app":"APP_URL",     #Enter app url here
        "network": False,
        "geoLocation": "FR",
        "devicelog": True,
        "visual" : True
    }

    return desired_caps

def runTest():
    if os.environ.get("LT_USERNAME") is None:
        # Enter LT username below if environment variables have not been added
        username = "username"
    else:
        username = os.environ.get("LT_USERNAME")
    if os.environ.get("LT_ACCESS_KEY") is None:
        # Enter LT accesskey below if environment variables have not been added
        accesskey = "accesskey"
    else:
        accesskey = os.environ.get("LT_ACCESS_KEY")

    # grid url
    gridUrl = "mobile-hub-internal.lambdatest.com/wd/hub"

    # capabilities
    desired_cap = getCaps()
    url = "https://"+username+":"+accesskey+"@"+gridUrl

    print("Initiating remote driver on platform: "+desired_cap["deviceName"]+" browser: "+" version: "+desired_cap["platformVersion"])
    driver = webdriver.Remote(
        desired_capabilities=desired_cap,
        command_executor= url
    )

    # run test
    print(driver.session_id)

    element = driver.switch_to.active_element
    active = element.get_attribute('label')

    if active != "Keyboard":
      element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="EnterWebsiteName")
      element.click()
      time.sleep(1) 

    element = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="EnterWebsiteName")
    element.clear()
    time.sleep(1)   

    element = driver.find_element(by=AppiumBy.CLASS_NAME, value="//XCUIElementTypeApplication[@name=\"chief.qaTvTestApp\"]/XCUIElementTypeWindow/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther")
    element.send_keys("https://ifconfig.me")    

    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    driver.execute_script('mobile: pressButton', { 'name': 'Down' })
    driver.execute_script('mobile: pressButton', { 'name': 'Down' })
    driver.execute_script('mobile: pressButton', { 'name': 'Down' })    

    element = driver.switch_to.active_element
    element.click()
    time.sleep(1)   

    driver.execute_script('mobile: pressButton', { 'name': 'Right' })
    element = driver.switch_to.active_element
    element.click()
    time.sleep(3)   

    driver.quit()   

if __name__ == "__main__":
    runTest()
