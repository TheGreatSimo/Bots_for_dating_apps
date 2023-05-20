#!/usr/bin/env python3 

from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt
import random , time

juba = opt()
juba.add_argument('--user-data-dir=/Users/dennismorales/desktop/accounts/data/1')


driver = uc.Chrome(executable_path='/usr/local/bin/chromedriver', options=juba) 
driver.implicitly_wait(10)
# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(70)
# driver.implicitly_wait(10)


