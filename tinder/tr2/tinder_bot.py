#!/usr/bin/env python3 

import random
import time
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options as opt

juba = opt()
juba.add_experimental_option("detach", True)


#driver = uc.Chrome(options=juba)
driver = uc.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(5)

# wait until log in 
time.sleep(120)

active_element = driver.switch_to.active_element



def dismiss_alert():
    """Dismiss any alert if any."""
    delay = 0.25

    # last possible id based div
    base_element = self.browser.find_element(By.XPATH, modal_manager)

    # try to deny see who liked you
    try:
        xpath = './/main/div/div/div[3]/button[2]'
        WebDriverWait(base_element, delay).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        deny_btn = base_element.find_element(By.XPATH, xpath)
        deny_btn.click()
        return "POPUP: Denied see who liked you"

    except NoSuchElementException:
        pass
    except TimeoutException:
        pass

    # Try to dismiss a potential 'upgrade like' popup
    try:
        # locate "no thanks"-button
        xpath = './/main/div/button[2]'
        base_element.find_element(By.XPATH, xpath).click()
        return "POPUP: Denied upgrade to superlike"
    except NoSuchElementException:
        pass

    # try to deny 'add tinder to homescreen'
    try:
        xpath = './/main/div/div[2]/button[2]'

        add_to_home_popup = base_element.find_element(By.XPATH, xpath)
        add_to_home_popup.click()
        return "POPUP: Denied Tinder to homescreen"

    except NoSuchElementException:
        pass

    # deny buying more superlikes
    try:
        xpath = './/main/div/div[3]/button[2]'
        deny = base_element.find_element(By.XPATH, xpath)
        deny.click()
        return "POPUP: Denied buying more superlikes"
    except NoSuchElementException:
        pass

    # try to dismiss match
    matched = False
    try:
        xpath = '//button[@title="Back to Tinder"]'

        match_popup = base_element.find_element(By.XPATH, xpath)
        match_popup.click()
        matched = True

    except NoSuchElementException:
        pass
    except:
        matched = True
        self.browser.refresh()

    if matched and self.may_send_email:
        try:
            EmailHelper.send_mail_match_found(self.email)
        except:
            print("Some error occurred when trying to send mail.")
            print("Consider opening an Issue on Github.")
            pass
        return "POPUP: Dismissed NEW MATCH"

    # try to say 'no thanks' to buy more (super)likes
    try:
        xpath = './/main/div/div[3]/button[2]'
        deny_btn = base_element.find_element(By.XPATH, xpath)
        deny_btn.click()
        return "POPUP: Denied buying more superlikes"

    except ElementNotVisibleException:
        # element is not clickable, probably cuz it's out of view but still there
        self.browser.refresh()
    except NoSuchElementException:
        pass
    except:
        # TBD add stale element exception for now just refresh page
        self.browser.refresh()
        pass

    # Deny confirmation of email
    try:
        xpath = './/main/div/div[1]/div[2]/button[2]'
        remindmelater = base_element.find_element(By.XPATH, xpath)
        remindmelater.click()

        time.sleep(3)
        # handle other potential popups
        self._handle_potential_popups()
        return "POPUP: Deny confirmation of email"
    except:
        pass

    # Deny add location popup
    try:
        xpath = ".//*[contains(text(), 'No Thanks')]"
        nothanks = base_element.find_element(By.XPATH, xpath)
        nothanks.click()
        time.sleep(3)
        # handle other potential popups
        self._handle_potential_popups()
        return "POPUP: Deny confirmation of email"
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




def swipe():
    time.sleep(1)
    # like 4 times and likes on time 
    """ swip just like a human """  
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)
    time.sleep(2)


def intercart():
    """ get the bio from the profile and save into a csv file """
    active_element.send_keys(Keys.ARROW_UP)
    time.sleep(1)
    active_element.send_keys(Keys.ARROW_DOWN)


def run_bot(num_swipes):
    """Run the bot for a specified number of swipes."""
    for i in range(100):
        try:
            intercart()
            swipe()
        except:
            dismiss_alert()



if __name__ == "__main__":
    # Run the bot for 10 swipes
    run_bot(100)

    # Close the webdriver
    driver.quit()

