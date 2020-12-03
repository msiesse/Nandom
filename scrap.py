import getpass
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

driver = Chrome()
SCROLL_PAUSE_TIME = 1

def openNetflix():
    driver.get('https://www.netflix.com/fr-en/login')

def SignIn(emailValue, passwordValue):
    email = driver.find_element_by_id("id_userLoginId")
    password = driver.find_element_by_id("id_password")
    signIn = driver.find_element_by_class_name("login-button")
    email.send_keys(emailValue)
    password.send_keys(passwordValue)
    signIn.click()

def selectProfile(id):
    profiles = driver.find_elements_by_class_name("profile-link")
    driver.get(profiles[id].get_attribute("href"))

def browseMovies():
    driver.get('https://www.netflix.com/browse/genre/34399?so=su')
    time.sleep(5)

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def main():
    credentials = open('credentials', 'r')
    lines = credentials.read().splitlines()
    email = lines[0]
    password = lines[1]
    profile = int(lines[2])
    openNetflix()
    SignIn(email, password)
    time.sleep(5)
    selectProfile(profile)
    time.sleep(5)
    browseMovies()
    driver.quit()

if __name__ == '__main__':
	main()