#!/usr/bin/env python3

import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
import time, random

juba = opt()

# Type your path here 

juba.add_argument('--user-data-dir=/home/juba/bots/bumble/tr1/data/1')
driver = uc.Chrome(options=juba)

time.sleep(3)

driver.get("https://bumble.com/app")

time.sleep(60)

driver.quit()



openers = [
    "Hey! How's it going?",
    "Hey! I couldn't help but notice your profile and had to say hi.",
    "Hi there! What's up?",
    "Hey! What's your favorite thing to do on weekends?",
    "Hi there! I noticed we have a similar taste in music.",
    "Hey, I think we have some common interests. Wanna chat?",
    "Hi there! I'm interested in getting to know you better. How's your day going?",
    "Hey! Your profile caught my eye. Mind if I say hi?"
]


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
    time.sleep(2)
    try:
        button = [Keys.RIGHT , Keys.LEFT ]
        random_button = random.choice(button)
        driver.switch_to.alert.send_keys(random_button)
    except:
        print("I din't found the right and left")
    time.sleep(1)


def send_message():
    """Send a random custom message if a match is found."""
    time.sleep(1)
    try:
        # Choose a random custom message from the list and replace the placeholder with the match's name
        message = random.choice(openers)

        # Find the message input field and send the custom message
        message_box = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/main/div[2]/article/div/footer/div[2]/div[1]/div/div/div/div/input")
        message_box.send_keys(message)
        time.sleep(1)
        message_box.send_keys(Keys.RETURN)
    except:
        pass

def run_bot():
    try:
        swipe() 
        try:
            send_message() 
        except:
            print("no match")
    except:
        dismiss_alert()

for i in range(1000):
    run_bot()
