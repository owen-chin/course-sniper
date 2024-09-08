from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os

load_dotenv()
# Make it return True if it successfully sniped the course and false if not
def auto_register(snipe):
    if not isinstance(snipe, str):
        raise TypeError("Input must be a string")
    
    url = "https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection=12024&indexList={}".format(snipe)
    chrome_profile_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    driver.get(url)
    try:
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys(os.getenv("NET_ID"))
        password.send_keys(os.getenv("PASSWORD"))

        #1
        login = driver.find_element(By.NAME, "submit")
        login.click()
        #2
        trust = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, 'trust-browser-button')))
        trust.click()
        #3

        # sidebar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'sidebar')))
        # init_dl_count = len(sidebar.find_elements(By.TAG_NAME, "dl"))
        # print(init_dl_count)

        add_course = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, 'submit')))
        add_course.click()

        # sidebar = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'sidebar')))
        # new_dl_count = len(sidebar.find_elements(By.TAG_NAME, "dl"))
        # print(new_dl_count)

        # if new_dl_count > init_dl_count:
        #     print("NEW CLASSSSSSSS ADDEDEDDEDE")
        #     return True
        # return False
    
    except Exception as e:
        print(e)
        return
   

    time.sleep(10)
    driver.quit()


