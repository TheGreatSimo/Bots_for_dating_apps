#!/usr/bin/env python3

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.common.keys import Keys 
import time


juba = uc.ChromeOptions()
juba.add_argument('--user-data-dir=/home/juba/bots/bumble/show/data/1')
driver = uc.Chrome(options=juba)

time.sleep(8)
driver.get("https://bumble.com/app")

time.sleep(60)
driver.quit()
active_element = driver.switch_to.active_element



def dismiss_alert():
    """ dismiss any alert if any """
    try:
        driver.switch_to.alert.dismiss()
    except:
        pass 

    try:
        box = driver.find_element(By.LINK_TEXT, value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]')
        box.click()
    except:
        pass


def swipe():
    """ swip just like a human """  
    time.sleep(1)
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(0.5)



def run_bot():
    try:
        swipe()
    except:
        dismiss_alert()

for i in range(1000):
    run_bot()



