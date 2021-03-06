from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
WEB_URL = os.environ['WEB_URL']

chrome_driver_path = "../ChromeDriver/chromedriver_94"
ser_obj = Service(chrome_driver_path)

options_obj = webdriver.ChromeOptions()
# chrome browser config. Disable all notifications
# prefs = {"profile.default_content_setting_values.notifications" : 2}
prefs = {}
options_obj.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=ser_obj, options=options_obj)
driver.get(WEB_URL)
sleep(2)

# accept_privacy = driver.find_element_by_xpath('//*[@id="c-364499427"]/div/div[2]/div/div/div[1]/button')
# driver.find_element_by_xpath("//div[contains(text(),'Add User')]")
accept_privacy = driver.find_element(By.XPATH, "//span[contains(text(),'I accept')]")
accept_privacy.click()

login_button = driver.find_element(By.XPATH, "//span[contains(text(),'Log in')]")
login_button.click()

sleep(1)
fb_login = driver.find_element(By.XPATH, "//span[contains(text(),'Login with Facebook')]")
fb_login.click()

#Switch to Facebook login window
sleep(1)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
# print(driver.window_handles) # array of available browser windows
print(driver.title)

# accepting cookies pop up
sleep(1)
accept_cookies = driver.find_element(By.XPATH, "//button[contains(text(),'Allow All Cookies')]")
accept_cookies.click()

# Login and hit enter
sleep(1)
email = driver.find_element(By.XPATH, "//*[contains(@name,'email')]")
password = driver.find_element(By.XPATH, "//*[contains(@name,'pass')]")
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)

# # Delay by 5 seconds to allow page to load.
# sleep(5)

# Allow location notification.
allow_location_button = False
while not allow_location_button:
    try:
        button = driver.find_element(By.XPATH, "//span[contains(text(),'Allow')]")
        allow_location_button = button
    except NoSuchElementException:
        print('allow_location_button not found')
        sleep(2)

allow_location_button.click()

# Disallow notifications
allow_notifications_button = driver.find_element(By.XPATH, "//span[contains(text(),'Enable')]")
allow_notifications_button.click()

# Search for SVG button icons
button_array = False
while not button_array:
    try:
        like_button = driver.find_elements(By.XPATH, "//*[name()='svg'][@class='Scale(.5) Expand']")
        if len(like_button) == 0:
            raise NoSuchElementException
        button_array = like_button
        print('button_array', button_array)
    except NoSuchElementException:
        print('button_array not found')
        sleep(2)

# Like button in array of elements
like_button = button_array[1]
# Run loop while True
swipe_left = True
total_likes = 0

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
while swipe_left:
    # Add a 1 second delay between likes.
    sleep(0.33)
    try:
        like_button.click()
        total_likes += 1
        print('Total likes: ' + str(total_likes))
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except (NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException):
        try:
            # match_popup = driver.find_element(By.CSS_SELECTOR, "span[class='D(f) W(100%) CenterAlign']")
            # match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup = driver.find_element(By.XPATH, "//span[contains(text(),'Keep swiping')]")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            try:
                popup = driver.find_element(By.XPATH, "//span[contains(text(),'No Thanks')]")
                popup.click()
            except NoSuchElementException:
                try:
                    popup = driver.find_element(By.XPATH, "//span[contains(text(),'Not interested')]")
                    popup.click()
                except NoSuchElementException:
                    try:
                        popup = driver.find_element(By.XPATH, "//span[contains(text(),'GO GLOBAL')]")
                        print('No more matches in the area error. Total likes: ' + str(total_likes))
                        swipe_left = False
                    except NoSuchElementException:
                        print('Repeating the loop...')
                        sleep(2)

driver.quit()
