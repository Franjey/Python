""" This program is used to automatically publish pictures on Instagram

Francisco Jurado"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
import autoit

"""
    Part A:  Log-in to Instagram in mobile version
"""
chrome_options = Options()
chrome_options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.instagram.com')

sleep(3)
driver.find_element_by_xpath("//button[text()='Iniciar sesión']").click()
sleep(3)
driver.find_element_by_name("username").send_keys("insta_dog123@fastmail.com")
driver.find_element_by_name("password").send_keys("medallas")
driver.find_element_by_xpath("//button[@type='submit']").click()
sleep(5)

try:
    driver.find_element_by_link_text("Ahora no").click()
    sleep(3)
except:
    print("'Install application message' button not found")

try:
    driver.find_element_by_xpath("//button[text()='Cancelar']").click()
    sleep(3)
except:
    print("'Add instagram to home screen' button not found")

try:
    driver.refresh()
    sleep(3)
    driver.find_element_by_xpath("//button[text()='Ahora no']").click()
    sleep(3)
except:
    print("Notifications button not found")

"""
    Part B:  Detecting pictures under the script's working directory subfolder "Pictures", and upload them to Instagram
"""
# Import the os module, used to navigate within directories
import os

# Get the current script's directory
x = os.getcwd()  # C:\Users\Francisco\PycharmProjects\Instagram

# Transforms the current script's directory into a Tuple
x = os.path.split(x)  # ('C:\\Users\\Francisco\\PycharmProjects', 'Instagram')

# Tranforms the Tuple into a List, and appends the subfolder 'Pictures'
x = list(x)
x.append("Pictures\\")  # ['C:\\Users\\Francisco\\PycharmProjects', 'Instagram', 'Pictures\\']

# Joins the List items
x = "\\".join(x)  # C:\Users\Francisco\PycharmProjects\Instagram\Pictures\

# Lists the directories inside the defined subfolder
x_dir = os.listdir(x)

# Iterates over the subfolder files and concatenates the subfolder path with the file names, creating a file relative path
# It also ignores the .txt files, because that one is supposed to keep a log of the uploaded ones.
for i, counter in enumerate(range(len(x_dir))):
    if x_dir[i].endswith(".txt"):
        pass
    else:
        pictureRelativePath = x + x_dir[i]
        print(counter, pictureRelativePath)
        logFile = open(x + "picturesLog.txt", "a")
        logFile.write(x_dir[i] + " - Uploaded on: " + str(datetime.datetime.now()) + "\n")
        driver.find_element_by_xpath("//span[@aria-label='Nueva publicación']").click()
        sleep(5)
        autoit.control_focus("Abrir", "[CLASS:Edit;INSTANCE:1]")  #  when the function input parameter's contains "Control", can use Advanced Mode in the control settings for a more precise search
        autoit.control_set_text("Abrir", "[CLASS:Edit;INSTANCE:1]", pictureRelativePath)
        sleep(2)
        autoit.control_click("Abrir", "[CLASS:Button;INSTANCE:1]")
        sleep(2)
        driver.find_element_by_xpath("//button[text()='Siguiente']").click()
        sleep(2)
        driver.find_element_by_xpath("//button[text()='Compartir']").click()
        sleep(5)
