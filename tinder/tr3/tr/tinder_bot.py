#!/usr/bin/env python3 


#from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt
import random , time



juba = opt()

juba.add_argument('--profile-directory=Profile 4')
juba.add_argument('--user-data-dir=/home/juba/.config/google-chrome/')


driver = uc.Chrome(options=juba) 
time.sleep(10)
# Navigate to url
driver.get("https://tinder.com/app/recs")












#time.sleep(10000)
time.sleep(8)












active_element = driver.switch_to.active_element



def dismiss_alert():
    """ handle any pop up if any """

    # Deny confirmation of email
    try:
        xpath = './/main/div/div[1]/div[2]/button[2]'
        remindmelater = driver.find_element(By.XPATH, xpath)
        remindmelater.click()
        time.sleep(3)
    except:
        pass

    # Deny add location popup
    try:
        xpath = ".//*[contains(text(), 'No Thanks')]"
        nothanks = driver.find_element(By.XPATH, xpath)
        nothanks.click()
        time.sleep(3)
    except:
        pass

    try:
        driver.switch_to.alert.dismiss()
    except:
        pass

    try:
        box = driver.find_element(By.XPATH, '//button/span[text()="Maybe Later" or text()="Not interested" or text()="No Thanks"]')
        box.click()
    except:
        pass

    try:
        driver.refresh()
    except:
        pass 



def intercart():
    """ get the bio from the profile and save into a csv file """
    active_element.send_keys(Keys.ARROW_UP)
    time.sleep(2)
    active_element.send_keys(Keys.ARROW_DOWN)


def go_through_picutre():
    for i in range(3):
        active_element.send_keys(Keys.SPACE)
        time.sleep(1)



def swipe():
    """ swip just like a human """  
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(2)
   

def send_message():
    """Send a random custom message if a match is found."""
    try:
        # Extract the match's name from the profile page
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[3]/div[2]')
        name = name.text.split()
        name = name[0]
        # Sending a message including a message saving hey 
        try:
            message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[3]/div[3]/form/textarea')
            message =  f"Hey {name}" 
            message_box.send_keys(message)
            time.sleep(3)
            message_box.send_keys(Keys.RETURN)

        except:
            message_box1 = driver.find_element(By.CSS_SELECTOR , '#s-1698539549')
            message =  f"Hey {name} "
            message_box.send_keys(message)
            time.sleep(1)
            message_box.send_keys(Keys.RETURN)
            
    except:
        print("No match")
        pass



def run_bot(num_swipes):
    """Run the bot for a specified number of swipes."""
    for i in range(1000):
        try:
            intercart()
            go_through_picutre()
            swipe()
            send_message()
        except:
            dismiss_alert()



if __name__ == "__main__":
    run_bot(100)
    driver.quit()

