import random
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as opt

juba = opt()
#juba.add_experimental_option("detach", True)


juba.add_argument('--profile-directory=Default')
juba.add_argument('--user-data-dir=/Users/dennismorales /Library/Application Support/Google/Chrome/')


driver = webdriver.Chrome(options=juba)
time.sleep(2)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(100)
