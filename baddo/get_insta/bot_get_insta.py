#!/usr/bin/env python3 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.common.keys import Keys 
import csv , re , random ,time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException

juba = opt()
juba.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=juba)
time.sleep(3)
driver.get("https://badoo.com")
driver.implicitly_wait(10)




email = "meleme6827@meidecn.com"
password = "Aissaoui@2007"


# like and dislike Xpaths 
like = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[1]/button'
dislike = '//*[@id="mm_cc"]/div[1]/section/div/div[2]/div/div[2]/div[2]/button'




active_element = driver.switch_to.active_element
find_bio = '/html/body/div[3]/div[1]/main/div[1]/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div/p'

# Define regular expressions for matching Instagram handles
regex1 = r'(?i)IG:\s*(\S+)'  # Matches "IG: " followed by non-whitespace characters
regex2 = r'(?i)(?:IG|Instagram)\s*:\s*(\S+)'  # Matches "IG: " or "Instagram:" followed by non-whitespace characters
regex3 = r'(?i)Insta:\s*(\S+)'  # Matches "Insta: " followed by non-whitespace characters
regex2 = r'(?i)(?:IG|Instagram)\s*:\s*(\S+)'  # Matches "IG: " or "Instagram:" followed by non-whitespace characters
regex4 = r"(?i)(?:IG|Instagram)\s*:?\s*([\w._]+)" # Matches variations of "IG" and "Instagram" followed by an optional colon and then captures the handle as a group



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
        try:
            password_input = driver.find_element(By.XPATH, '//*[@id="signin-password"]')
            password_input.send_keys(password)
        except:
            print("didn't fond xpath ")
        try:
            time.sleep(2)
            enter = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/section/div/div/div[1]/form/div[5]/div/div[1]/button").click()
        except:
            print("can't send the keys now")

        time.sleep(10)
    except:
        print("no password")
        pass


def dismiss_alert():
    """ dismiss any alert if any """

    try:
        driver.find_element(By.XPATH, "/html/body/aside/section/div[1]/div/div/section/div/div/div/div[2]/button").click()
    except:
        pass
    try:
        driver.switch_to.alert.dismiss()
    except:
        pass 
    try:
        box = driver.find_element(By.XPATH, value='//button/span[text()="Maybe Later"] | //button/span[text()="Not interested"] | //button/span[text()="No Thanks"]')
        box.click()
    except:
        pass


def swipe():
    """ swip just like a human """  
    try:
        like = Keys.NUMPAD1
    except:
        print("cant't find 1 ")
    try:
        dislike = Keys.NUMPAD2
    except:
        print("coudn't find 2")
    try:
        button = [like,dislike ]
    except:
        print("no list no likes and dislekes")
    random_button = random.choice(button)
    try:
        active_element.send_keys(random_button)
    except:
        print("can't click the button")
    time.sleep(1)


def get_bio():
    """ get the bio from the profile and save into a csv file """
    time.sleep(1)
    # find bio
    try:
        bio = driver.find_element(By.XPATH,find_bio)
        bio = bio.text
        write_file(bio)
    except:
        print("no bio to be found")
        pass


def extract_instagram_handle(bio):
    ig_handle1 = re.search(regex1, bio)
    ig_handle2 = re.search(regex2, bio)
    ig_handle3 = re.search(regex3, bio)
    ig_handle4 = re.search(regex4, bio)

    ig_handle = ig_handle1 or ig_handle2 or ig_handle3 or ig_handle4
    if ig_handle:
        return ig_handle.group(1)
    else:
        return None

def write_file(bio):
    with open('instagram_handles.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:  # Check if the file is empty
            writer.writerow(['Bio', 'Instagram'])
        ig_handle = extract_instagram_handle(bio)
        writer.writerow([bio, ig_handle if ig_handle else ''])


login()

def run_bot():
    dismiss_alert()
    get_bio()
    time.sleep(1)
    swipe()


while True:
    run_bot()
