from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

FB_EMAIL = "lookatemail@gmail.com"
FB_PASSWORD = "rybzij-hyvzyd-7mArbe"

chrome_driver_path = "../ChromeDriver/chromedriver_94"
ser_obj = Service(chrome_driver_path)
driver = webdriver.Chrome(service=ser_obj)

driver.get("http://www.tinder.com")

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
print(driver.window_handles) # array of available browser windows
print(driver.title)

# accepting cookies pop up
sleep(1)
accept_cookies = driver.find_element(By.XPATH, "//button[contains(text(),'Allow All Cookies')]")
accept_cookies.click()

# Login and hit enter
sleep(1)
email = driver.find_element(By.XPATH, "//*[contains(@name,'email')]")
password = driver.find_element(By.XPATH, "//*[contains(@name,'pass')]")
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
