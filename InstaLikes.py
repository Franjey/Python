from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
assert 'Instagram' in driver.title

# Log in Page
'''
<a href="continue.html">Continue</a>
continue_link = driver.find_element_by_link_text('Continue')
continue_link = driver.find_element_by_partial_link_text('Conti')
'''
driver.find_element_by_link_text('Log in').click()
sleep(4)

# Fill in the Log-in information
driver.find_element_by_name("username").send_keys("insta_dog123@fastmail.com")
driver.find_element_by_name("password").send_keys("medallas")
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(4)

# If any notification button appears, handle them
try:
    driver.find_element_by_link_text("Not Now").click()
    sleep(4)
except:
    print("The link text was not found")

try:
    driver.find_element_by_xpath("//button[text()='Not Now']").click()
    sleep(4)
except:
    print("The button text was not found")

# Like Posts
for i in range(3):
    body_elem = driver.find_element_by_tag_name('body')
    body_elem.send_keys(Keys.END)
    sleep(2)
    body_elem.send_keys(Keys.HOME)
    sleep(2)

heart_elements = driver.find_elements_by_xpath("//span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
print("Hearts found: " + str(len(heart_elements)))

for i, heart in enumerate(range(len(heart_elements)), 1):
    print(i, len(heart_elements))
    heart_elements[heart].click()
    sleep(2)