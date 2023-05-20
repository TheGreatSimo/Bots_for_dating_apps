#!/usr/bin/env python3 

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
import random , time





driver = uc.Chrome() 
#driver = webdriver.Chrome() 






driver.implicitly_wait(10)
# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(100)


