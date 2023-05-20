#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
import time
import re , random 

juba = opt()
juba.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=juba)
time.sleep(3)
driver.get("https://badoo.com")
driver.implicitly_wait(10)






email = "Your email or number without any spaces"
password = "Your password without any spaces"





# like and dislike Xpaths 
like = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/button'
dislike = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/button'

def login():

    try:
        time.sleep(3)
        sign_in = driver.find_element(By.XPATH,'//*[@id="header"]/div/div[2]/div/div/a' )
        sign_in.click() 
    except:
        print("sign in failed")

    try:
        time.sleep(3)
        email_input = driver.find_element(By.XPATH,'//*[@id="signin-name"]')
        email_input.send_keys(email)
    except:
        print("no email")

    try:
        time.sleep(2)
        password_input = driver.find_element(By.XPATH , '//*[@id="signin-password"]') 
        password_input.send_keys(password + Keys.ENTER)
    except:
        print(" no password")

    try:
        time.sleep(2)
        submit_button = driver.find_element(By.XPATH , '//*[@id="signin-submit"]/button')
        submit_button.click()
    except:
        print("no submit button ")
    time.sleep(30)

login()


def dismiss_alert():
    """Dismiss any alert dialogs present on the page"""
    try:
        time.sleep(1)
        pop_up = driver.find_element(By.XPATH ,'/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/button')
        pop_up.click()
    except:
        pass 
    try:
        # Handle alert dialog
        alert = driver.switch_to.alert
        alert.dismiss()

    except NoAlertPresentException:
        pass

    except UnexpectedAlertPresentException:
        # Handle modal or overlay
        overlay = driver.find_element_by_css_selector("div[class^='overlay']")
        if overlay:
            overlay.click()

        # Handle dialog
        try:
            dialog = driver.find_element_by_css_selector("div[class*='dialog']")
            close_button = dialog.find_element_by_css_selector("button[class*='close'], a[class*='close']")
            close_button.click()
        except NoSuchElementException:
            pass

    # Handle any nested pop-ups
    try:
        handle_popups(driver)
    except:
        pass



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
    try:
        like_dislike()
    except:
        dismiss_alert()

while True:
    run_bot()
