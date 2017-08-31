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
login.send_keys('YOUR FACEBOOK LOGIN HERE')
password = driver.find_element_by_css_selector('#pass')
password.send_keys('YOUR PASSWORD HERE')
password.send_keys(Keys.RETURN)
time.sleep(2)

# Go to timeline
username = sys.argv[1]
url = "https://www.facebook.com/" + username + "/allactivity?privacy_source=activity_log&log_filter=cluster_11"
driver.get(url)
time.sleep(2)

# Grab the text of each post

for i in range(0,30):

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    timeline_posts = driver.find_elements_by_xpath(".//div[@class='fsm']")

    for post in timeline_posts:
        print (post.text)
        time.sleep(2)

driver.quit()
