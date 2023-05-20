import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time ,random
from selenium.webdriver.chrome.options import Options as opt

juba = opt()
#path = '/usr/bin/chromedriver'
juba.add_experimental_option("detach", True)
juba.add_argument('--profile-directory=Default')
juba.add_argument('--user-data-dir=C:\\Users\\Alex\\AppData\\Local\\Google\\Chrome\\User Data\\')
driver = uc.Chrome(options=juba)
time.sleep(5)

# Navigate to url
driver.get("https://tinder.com/app/recs")
time.sleep(20)
active_element = driver.switch_to.active_element

haja = 

def dismiss_alert():
    """Dismiss any alert if any."""
    delay = 0.25

    # try to deny see who liked you
    try:
        xpath = './/main/div/div/div[3]/button[2]'
        WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        deny_btn = driver.find_element(By.XPATH, xpath)
        deny_btn.click()
    except NoSuchElementException:
        pass

    except TimeoutException:
        pass
    except:
        pass

    # Try to dismiss a potential 'upgrade like' popup
    try:
        # locate "no thanks"-button
        xpath = './/main/div/button[2]'
        driver.find_element(By.XPATH, xpath).click()
    except NoSuchElementException:
        pass

    # try to deny 'add tinder to homescreen'
    try:
        xpath = './/main/div/div[2]/button[2]'
        add_to_home_popup = driver.find_element(By.XPATH, xpath)
        add_to_home_popup.click()

    except NoSuchElementException:
        pass

    # deny buying more superlikes
    try:
        popup1 = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/button[2]/div[2]/div[2]')
        popup1.click()
    except:
        pass


    # try to say 'no thanks' to buy more (super)likes
    try:
        xpath = './/main/div/div[3]/button[2]'
        deny_btn = driver.find_element(By.XPATH, xpath)
        deny_btn.click()

    except ElementNotVisibleException:
        # element is not clickable, probably cuz it's out of view but still there
       driver.refresh()
    except NoSuchElementException:
        pass
    except:
        # TBD add stale element exception for now just refresh page
        driver.refresh()
        pass

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



def swipe():
    """ swip just like a human """
    time.sleep(100)
    button = [Keys.RIGHT , Keys.LEFT ]
    random_button = random.choice(button)
    active_element.send_keys(random_button)





def send_message():
    """Send a random custom message if a match is found."""
    time.sleep(10)
    try:
        # Extract the match's name from the profile page
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[3]/div[2]')
        name = name.text.split()
        name = name[0]
        # Choose a random custom message from the list and replace the placeholder with the match's name
#        message =  f"Hey {name} add my instagram marianaaaluv"
        # Find the message input field and send the custom message
        try:
            message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[3]/div[3]/form/textarea')
            greetings = ['Hi there', 'Yo', 'What\'s up', 'Hey', 'Hello', 'Howdy', 'Hiya', 'Heya', 'Sup', 'Hi']
            hey = random.choice(greetings)

            message =  f"{hey} {name} add my instagram marianaaaluv"
            time.sleep(30)
            message_box.send_keys(message)
        except:
            message_box1 = driver.find_element(By.CSS_SELECTOR , '#s-1698539549')
            message =  f"Hey {name} add my instagram marianaaaluv"
            message_box.send_keys(message)
            time.sleep(30)
            message_box.send_keys(Keys.RETURN)
            
    except:
        print("No match")
        pass








def run_bot(num_swipes):
    """Run the bot for a specified number of swipes."""
    for i in range(num_swipes):
        try:
            swipe()
            send_message()
        except:
            dismiss_alert()






if __name__ == "__main__":
    # Run the bot for 10 swipes
    run_bot(100)

    # Close the webdriver
    driver.quit()




