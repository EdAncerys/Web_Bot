from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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

