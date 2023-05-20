#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import random


driver = webdriver.Chrome()
driver.get("https://badoo.com")
driver.implicitly_wait(10)


email = "0668646370"
password = "Aissaoui@2007"


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
