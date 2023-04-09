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


    # Search for items- in list
    scraped_products = {}

    for restaurant in stores:
        search = driver.find_element(By.ID, "search-suggestions-typeahead-input")
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        search.send_keys(restaurant)  
        search.send_keys(Keys.RETURN) 

        time.sleep(5)

        # Scraping Restaurant- Get first search result
        results = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]')
        name = results.find_element(By.TAG_NAME, 'a')
        print(name.text)

        # click on restaurant and navigate to menu page
        time.sleep(10)
        link = driver.find_element(By.LINK_TEXT, name.text)
        driver.execute_script('arguments[0].click()', link)

        time.sleep(10)

        # Handle pop ups- find a way to disable them so that menu is not messed up
        
        # Process Menu- TO DO
        # Look for cheapest, add to dictionary

        # Navigate back to list of restaurants
        driver.back()
        time.sleep(10)


    return scraped_products



address = "125 Spence St, College Station" #Zachry Engineering Building
item = "burgers"
stores = ["McDonalds", "Whataburger", "Hopdoddy"]
uberEats(stores, item, address)