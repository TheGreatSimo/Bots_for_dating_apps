#!/usr/bin/env python3 

import random
import time
from selenium import webdriver
#import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt

juba = opt()

juba.add_experimental_option("detach", True)
juba.add_argument('--profile-directory=Profile 4')
juba.add_argument('--user-data-dir=/home/juba/.config/google-chrome/')
juba.add_argument('headless')
juba.add_argument('window-size=1200x600')

#driver = uc.Chrome(options=juba)

driver = webdriver.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(5)

active_element = driver.switch_to.active_element


def dismiss_alert():
    # Deny confirmation of email
    try:
        xpath = './/main/div/div[1]/div[2]/button[2]'
        remindmelater = driver.find_element(By.XPATH, xpath)
        remindmelater.click()
        time.sleep(3)
    except:
        pass

    # Deny add location popup
    try:
        xpath = ".//*[contains(text(), 'No Thanks')]"
        nothanks = driver.find_element(By.XPATH, xpath)
        nothanks.click()
        time.sleep(3)
    except:
        pass

    try:
        driver.switch_to.alert.dismiss()
    except:
        pass

    try:
        box = driver.find_element(By.XPATH, '//button/span[text()="Maybe Later" or text()="Not interested" or text()="No Thanks"]')
        box.click()
    except:
        pass

    try:
        driver.refresh()
    except:
        pass 



def swipe():
    time.sleep(1)
    # like 4 times and likes on time 
    """ swip just like a human """  
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(1)


def run_bot(num_swipes):
    """Run the bot for a specified number of swipes."""
    for i in range(1000):
        try:
            swipe()
        except:
            dismiss_alert()



if __name__ == "__main__":
    # Run the bot for 10 swipes
    run_bot(100)

    # Close the webdriver
    driver.quit()

