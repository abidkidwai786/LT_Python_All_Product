# Tested on python3, Selenium 4.9.0, Appium-Python-Client 2.2.0

from appium import webdriver
# --- FIX 1: Import AppiumOptions for modern W3C/Appium binding ---
from appium.options.common.base import AppiumOptions
from selenium.webdriver.common.by import By
import time


# Define credentials (using user-provided values)
USERNAME = ""
ACCESS_KEY = ""
# URL template is defined here, will be formatted before use
MOBILE_HUB_URL_TEMPLATE = "https://{USERNAME}:{ACCESS_KEY}@mobile-hub.lambdatest.com/wd/hub"


def startingTest(caps_list):
    """
    Initializes the Appium WebDriver and executes the mobile test script.
    """
    print(f"Starting test")

    # Get the first set of capabilities dictionary
    desired_cap_dict = caps_list[0].copy()

    # --- FIX 2: Prepare the AppiumOptions object ---
    options = AppiumOptions()

    # Extract LambdaTest capabilities nested under 'lt:options'
    lt_options = desired_cap_dict.get('lt:options', {})

    # Load all capabilities into the AppiumOptions object
    for key, value in lt_options.items():
        options.set_capability("lt:options", lt_options)

    # Extract device info for logging
    device_name = options.get_capability('deviceName')
    platform_version = options.get_capability('platformVersion')
    print(
        f"deviceName {device_name}, platformVersion {platform_version}"
    )

    # --- FIX 3: Correctly format the command_executor URL with credentials ---
    formatted_url = MOBILE_HUB_URL_TEMPLATE.format(
        USERNAME=USERNAME,
        ACCESS_KEY=ACCESS_KEY
    )

    driver = None # Initialize driver variable
    try:
        # The FIX: Pass 'options' object instead of 'desired_capabilities' keyword
        driver = webdriver.Remote(command_executor=formatted_url, options=options)
    except Exception as e:
        print(f"Error creating WebDriver: {e}")
        return

    try:
        print(f"driver created")
        time.sleep(10)

        ctx = driver.current_context
        print("ctx", ctx)
        sessionId = driver.session_id
        print("sessionId", sessionId)
        isKeyBoardShown = driver.is_keyboard_shown()
        print(f"isKeyboardShown {isKeyBoardShown}")
        isLocked = driver.is_locked()
        print("isLocked", isLocked)
        isInstalled = driver.is_app_installed("com.example.QAapp")
        print("isInstalled", isInstalled)

        print(driver.page_source)
        # Using find_element returns an element; calling .click() on it performs the action
        driver.find_element(By.ID, "com.example.QAapp:id/webpage").click()
        print("Clicked 'webpage' element")
        time.sleep(2)

        website_name_id = "com.example.QAapp:id/websiteName"
        find_button_id = "com.example.QAapp:id/findButton"

        driver.find_element(By.ID, website_name_id).send_keys(
            "ThisIsDemoText"
        )
        driver.find_element(By.ID, website_name_id).clear()
        elem = driver.find_element(By.ID, find_button_id)
        print("Found 'findButton' element:", elem)

        driver.find_element(By.ID, website_name_id).click()
        params = {"command": "input-text", "text": "thisIsMyText"}
        result = driver.execute_script("lambda-adb", params)
        print("ADB execution result:", result)
        time.sleep(2)

        driver.find_element(By.ID, website_name_id).send_keys(
            "https://www.ifconfig.me"
        )
        # find_element by ID requires the full package name if it's the Appium default strategy
        # Using the full ID here based on previous usage
        driver.find_element(By.ID, find_button_id).click()
        time.sleep(2)

        driver.find_element(By.ID, website_name_id).send_keys(
            "https://google.com"
        )
        driver.find_element(By.ID, find_button_id).click()
        time.sleep(2)

        # Check for tunnel capability using the options object
        if options.get_capability("tunnel"):
            driver.find_element(By.ID, website_name_id).send_keys(
                "http://localhost.lambdatest.com:8001"
            )
            driver.find_element(By.ID, find_button_id).click()
            time.sleep(5)

        driver.orientation = "LANDSCAPE"

        print("Quitting test")
        driver.quit()
    except Exception as e:
        print(f"An error occurred during test execution: {e}")
        if driver:
            driver.quit()
        else:
            print("Driver was not initialized, skipping quit.")


# Define capabilities list
caps = [
    {
        "lt:options": {
            "w3c": True,
            "platformName": "android",
            # "allowInvisibleElements": True,
            "deviceName": "Galaxy S24",
            "platformVersion": "15",
            "app": "lt://APP10160211661762881095332257",
            "appiumVersion": "2.16.2",
            # "devicelog": True,
            # "visual": True,
            # "network": True,
            # "tunnel": False,
            # "video": True,
            # "isRealMobile": False,
        },
    }
]

# Execute the test
if __name__ == "__main__":
    startingTest(caps)