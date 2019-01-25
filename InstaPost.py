""" This program is used to automatically publish pictures on Instagram"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.instagram.com')

sleep(3)
driver.find_element_by_xpath("//button[text()='Log In']").click()
sleep(3)
driver.find_element_by_name("username").send_keys("insta_dog123@fastmail.com")
driver.find_element_by_name("password").send_keys("medallas")
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)

try:
    driver.find_element_by_link_text("Not Now").click()
    sleep(3)
except:
    print("'Install application message' button not found")

try:
    driver.find_element_by_xpath("//button[text()='Cancel']").click()
    sleep(3)
except:
    print("'Add instagram to home screen' button not found")

try:
    driver.refresh()
    sleep(3)
    driver.find_element_by_xpath("//button[text()='Not Now']").click()
    sleep(3)
except:
    print("Notifications button not found")


### selenium.common.exceptions.WebDriverException: Message: unknown error: cannot focus element
driver.find_element_by_xpath("//span[@aria-label='New Post']").send_keys(os.getcwd() + "IBM.jpeg")
sleep(2)
