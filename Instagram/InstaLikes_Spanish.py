""" This program is used to automatically like pictures on Instagram.  Instagram in Spanish.

Francisco Jurado"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from sklearn import exceptions
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
assert 'Instagram' in driver.title

login_link = driver.find_element_by_link_text('Inicia sesión').click()
sleep(4)

user_form = driver.find_element_by_name('username').send_keys('insta_dog123@fastmail.com')
password_form = driver.find_element_by_name('password').send_keys('medallas')
driver.find_element_by_xpath("//button[@type='submit']").click()

sleep(4)

try:
    driver.find_element_by_link_text('Ahora no').click()
except:
    print("El boton no se encontro 2")

sleep(4)

try:
    driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
except:
    print("El boton no se encontro")

body_elem = driver.find_element_by_tag_name('body')

for i in range(3):
    body_elem.send_keys(Keys.END)
    sleep(2)
    body_elem.send_keys(Keys.HOME)
    sleep(2)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(5)

# find all heart links
# hearts = driver.find_elements_by_xpath("//span[@class='fr66n']")
# hearts = driver.find_elements(By.XPATH, '//button[./span[@aria-label="Me gusta"][@class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]]')
# hearts = driver.find_elements(By.XPATH, '//button[./span[@class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]]')
hearts = driver.find_elements(By.XPATH, '//button[./span[@aria-label="Me gusta"]]')

print(range(len(hearts)))

for i, heart in enumerate(hearts):
    print('{}/{}'.format(i, len(hearts)))
    heart.click()
    sleep(2)

'''
for i, h in enumerate(range(len(hearts))):
    try:
        sleep(3)
        xpathIndex = "(//button[./span[@aria-label='Me gusta'][@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']])[{}]".format(h+1) # xpath index start from 1 not 0
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpathIndex)))
        ActionChains(driver).move_to_element(hearts[h]).click(hearts[h]).perform()
        print(i, len(hearts))
    except exceptions.StaleElementReferenceException as e:
        raise e
'''
