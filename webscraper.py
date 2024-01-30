from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import os
import sys
import datetime as dt
from bs4 import BeautifulSoup as soup
from urllib import parse
import os

curr_dir = os.path.dirname(sys.argv[0])
curr_dir = os.path.abspath(curr_dir)
chrome_options = Options()
prefs = {"download.default_directory" : f'{curr_dir}'}
chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--window-size=1440, 900")

mydriver = webdriver.Chrome(chrome_options=chrome_options)
    
    

for num in range(20):
    url = f"https://www.zillow.com/homes/CA_rb/{num}_p/"
    mydriver.get(url)
    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = mydriver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1
    while True:
        # scroll one screen height each time
        mydriver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height cansion change after we scrolled the page
        scroll_height = mydriver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break