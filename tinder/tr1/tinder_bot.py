#!/usr/bin/env python3 

import random
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt

juba = opt()
#juba.add_experimental_option("detach", True)


"""
juba.add_argument('--profile-directory=Default')
juba.add_argument('--user-data-dir=/Users/dennismorales /Library/Application Support/Google/Chrome/')
"""


juba.add_argument('--profile-directory=Profile 4')
juba.add_argument('--user-data-dir=/home/juba/.config/google-chrome/')






driver = webdriver.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(5)

active_element = driver.switch_to.active_element



def dismiss_alert():
    """Dismiss any alert if any."""
    delay = 0.25
    try:
        driver.switch_to.alert.dismiss()
    except:
        pass

    try:
        box = driver.find_element(By.XPATH, '//button/span[text()="Maybe Later" or text()="Not interested" or text()="No Thanks"]')
        box.click()
    except:
        pass




def swipe():
    time.sleep(1)
    # like 4 times and likes on time 
    """ swip just like a human """  
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(2)


def intercart():
    """ get the bio from the profile and save into a csv file """
    active_element.send_keys(Keys.ARROW_UP)
    time.sleep(1)
    active_element.send_keys(Keys.ARROW_DOWN)


def run_bot(num_swipes):
    """Run the bot for a specified number of swipes."""
    for i in range(100):
        try:
            intercart()
            swipe()
        except:
            dismiss_alert()



if __name__ == "__main__":
    # Run the bot for 10 swipes
    run_bot(100)

    # Close the webdriver
    driver.quit()

