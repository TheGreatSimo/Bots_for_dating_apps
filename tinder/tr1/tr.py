#!/usr/bin/env python3 

import random,time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

juba = opt()

juba.add_argument('--user-data-dir=/Users/dennismorales/Desktop/accounts/data/1')

driver = uc.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(5)


