from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
import random

# initialize the webdriver and variables
load_dotenv()
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
COURSE_NAME = os.getenv('COURSE_NAME')
CLASS_DURATION = int(os.getenv('CLASS_DURATION'))

URL = 'https://student.iclicker.com/#/login'

driver = webdriver.Chrome()

driver.get(URL)

time.sleep(2)

driver.find_element(By.ID, 'userEmail').send_keys(USERNAME)
driver.find_element(By.ID, 'userPassword').send_keys(PASSWORD)

time.sleep(2)

driver.find_element(By.ID, 'sign-in-button').click()
time.sleep(2)

try:
    course_link = driver.find_element(By.XPATH, f"//label[contains(text(), '{COURSE_NAME}')]/..")
    course_link.click()
except Exception as e:
    print("Error clicking on course link by label text:", str(e))
    driver.quit()

time.sleep(2)


def join_class():
    while True:
        try:
            driver.find_element(By.ID, 'btnJoin').click()
            break
        except Exception as e:
            pass


join_class()

# start a stopwatch to keep track of time
start_time = time.time()

while True:
    end_time = time.time()
    all_text = driver.execute_script("return document.body.textContent")
    # checking if prof accidentally stopped the class
    if "Score" in all_text:
        join_class()

    if "was not recorded" in all_text:
        try:
            driver.find_element(By.XPATH, f"//button[contains(text(), 'Ok')]").click()
        except Exception as e:
            pass

    # main logic to answer the questions
    index = random.randint(0, 3)
    OPTIONS = ['A', 'B', 'C', 'D']
    try:
        driver.find_element(By.XPATH, f"//button[contains(text(), '{OPTIONS[index]}')]").click()
    except Exception as e:
        pass

    time.sleep(5)
    if end_time - start_time > CLASS_DURATION:
        break
