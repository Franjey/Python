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

counter = 0

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
    driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()
except:
    print("El boton no se encontro")

body_elem = driver.find_element_by_tag_name('body')

'''for _ in range(3):
    body_elem.send_keys(Keys.END)
    sleep(2)
    body_elem.send_keys(Keys.HOME)
    sleep(2)
'''
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

sleep(5)
# find all heart links
hearts = driver.find_elements_by_xpath("//span[@class='fr66n']")
print(range(len(hearts)))

'''for h in range(len(hearts)):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, hearts[h])));
        ActionChains(driver).move_to_element(hearts[h]).click(hearts[h]).perform()
        counter += 1
        print(str(counter) + "/" + str(len(hearts)))
    except exceptions.StaleElementReferenceException as e:
        raise e
'''
for h in range(len(hearts)):
    try:
        sleep(10)
        driver.implicitly_wait(120)
        ActionChains(driver).move_to_element(hearts[h]).click(hearts[h]).perform()
        counter += 1
        print(str(counter) + "/" + str(len(hearts)))
    except exceptions.StaleElementReferenceException as e:
        raise e
