import csv
#from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
'''
def init(s):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.heb.com/')
    # Get cookies for request session
    cookies = browser.get_cookies()
    browser.quit()
    # Creating a session
    s.session = requests.Session()
     # PLace cookies in the session cookie jar
    [requests.Session().cookies.set(cookie['name'], cookie['value']) for cookie in cookies]

def getLinks(s, product):
    url = "https://www.heb.com/search/?q=" + product
    page = s.session.get(url)
    print(page)
    #soup = BeautifulSoup(page.text, 'html.parser')
'''
#init(s)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
driver.get("https://www.heb.com/")

# this is the amount of time the website will show up 
time.sleep(5)

#soup = BeautifulSoup(driver.page_source,features="html.parser")
#getLinks("bread")

