#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time
import re , random 


juba = opt()
path = '/usr/bin/chromedriver'
juba.add_experimental_option("detach", True)
juba.add_argument('--profile-directory= here your profile without any spaces')
juba.add_argument('--user-data-dir= here you path without any spaces')
driver = webdriver.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://us1.badoo.com/encounters")

time.sleep(20)


# like and dislike Xpaths 
like = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/button'
dislike = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/button'



def dismiss_alert():
    """Dismiss any alert dialogs present on the page"""
    try:
        alert = driver.switch_to.alert
        alert.dismiss()
    except NoAlertPresentException:
        pass
    except UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        alert.dismiss()
        dismiss_alert()



def like_dislike():

    for i in range(10):
        time.sleep(3)
        if i % 5 == 4:  # execute the second choice once every five iterations
            dislike_button = driver.find_element(By.XPATH , dislike)
            dislike_button.click()

        else:
            """ like 4 times """
            like_button = driver.find_element(By.XPATH , like)
            like_button.click()


def run_bot():
    dismiss_alert()
    like_dislike()

for i in range(3):
    run_bot()
