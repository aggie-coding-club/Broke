from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

import time

def uberEats(stores : list, item : str, address: str) -> dict:
    '''
    Locate address bar
    Enter address, hit enter
    Locate search bar
    Send text, hit enter
    Find the restaurant title, click on it 
    Go through the menu, find keywords that matches searched item
    Return a dictionary of store name as the key, and tuple as value
    {"Hopdoddy" : ("cheeseburger", 10.99)}

    '''
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
    driver.get("https://www.ubereats.com/")
    driver.maximize_window()


    # Search location and navigate to next page
    location = driver.find_element(By.ID, "location-typeahead-home-input")
    location.clear()
    location.send_keys(address)
    location.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="location-typeahead-home-item-0"]').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))

    # Search for items
    items = driver.find_element(By.ID, "search-suggestions-typeahead-input")
    items.clear()
    items.send_keys(item)  
    items.send_keys(Keys.RETURN) 

    time.sleep(5) 

    scraped_products = {}

    # Get Restaurants
    restaurants = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]/div')
    for restaurant in restaurants:
        name = restaurant.find_element(By.XPATH, './div[1]/a/h3')
        print(name.text)
        # click on restaurants
        # find menu and process data
        # go back and click on the next one


    print("Yay")
    return scraped_products



address = "125 Spence St, College Station" #Zachry
item = "burgers"
uberEats([], item, address)