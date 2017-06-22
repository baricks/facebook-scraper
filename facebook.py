from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, sys
import time
import threading
import shutil
import requests

# Set up Driver
driver = webdriver.PhantomJS()
driver.get("http://www.facebook.com/login")

# Log into Facebook
login = driver.find_element_by_css_selector('#email')
login.send_keys('ADD YOUR FB LOGIN HERE')
password = driver.find_element_by_css_selector('#pass')
password.send_keys('ADD YOUR FB PASSWORD HERE')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to timeline
username = sys.argv[1]
url = "https://www.facebook.com/" + username + "/timeline"
driver.get(url)
time.sleep(2)

# Grab the text of each post

for i in range(0,10):

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    timeline_posts = driver.find_elements_by_css_selector('p')

    for post in timeline_posts:
        text = post.text.encode('utf-8')
        print(text)
        time.sleep(2)

driver.quit()
