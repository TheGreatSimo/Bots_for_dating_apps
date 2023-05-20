#!/usr/bin/env python3

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
import random
import time


juba = opt()


juba.add_argument('--profile-directory=Default')
juba.add_argument('--user-data-dir=C:\\Users\\Mert\\AppData\\Roaming\\dolphin_anty\\browser_profiles\\84231405\\data_dir')

driver = uc.Chrome(options=juba)

time.sleep(8)
driver.get("https://bumble.com/app")

time.sleep(10)
active_element = driver.switch_to.active_element



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
        box = driver.find_element(By.XPATH, '//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]')
        box.click()
    except:
        pass


def swipe():
    """ swipe just like a human """  
    time.sleep(1)
    button = [Keys.RIGHT, Keys.LEFT]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(0.5)



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
            pass
    except Exception as e:
        print(f"Error: {e}")
        dismiss_alert()

for i in range(1000):
    run_bot()

driver.quit()

