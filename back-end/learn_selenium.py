import csv
#from bs4 import BeautifulSoup
from selenium import webdriver
import time

option = webdriver.ChromeOptions()
#option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')

driver = webdriver.Chrome("./chromedriver", options=option)
driver.get("https://www.heb.com/")

# this is the amount of time the website will show up 
time.sleep(10)