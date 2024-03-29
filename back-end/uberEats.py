from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import re

import time

def uberEats(stores : list[str], item : str, address: str) -> dict[str, tuple]:
    """Uses UberEats to find the price of the requested\n
    item at different restaurants

    Parameters
    ----------
    stores : list
        List of the stores to be scraped
    item : str
        The item to be searched for
    address : str
        The address of the user to be used in UberEats

    Returns
    -------
    dict
        Dictionary containing the item, along with its price, found at each location.\n
        Only keeps the single item with the lowest price from each location. The\n
        dictionary is in the form {store name : (item name at store, price)}
    """
    
    # Driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.ubereats.com/")
    driver.maximize_window()

    # Search location and navigate to next page
    location = driver.find_element(By.ID, "location-typeahead-home-input")
    location.clear()
    location.send_keys(address)
    location.send_keys(Keys.RETURN)
    #time.sleep(5)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="location-typeahead-home-item-0"]')))
    driver.find_element(By.XPATH, '//*[@id="location-typeahead-home-item-0"]').click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))


    # Search for items- in list
    scraped_products = {}

    for restaurant in stores:
        search = driver.find_element(By.ID, "search-suggestions-typeahead-input")
        #time.sleep(1)
        search.send_keys(Keys.CONTROL + "a")
        search.send_keys(Keys.DELETE)
        #time.sleep(2)
        search.send_keys(restaurant)  
        search.send_keys(Keys.RETURN) 

        time.sleep(2)

        # Scraping Restaurant- Get first search result //*[@id="main-content"]/div/div/div[2]/div/div[2]/div[1]
        # //*[@id="main-content"]/div/div/div[2]/div/div[2]/div[2]
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]')))
        results = driver.find_element(By.XPATH, '//*[@id="main-content"]/div/div/div[2]/div/div[2]')

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        names = results.find_elements(By.TAG_NAME, 'a')
        name = ''
        for _name in names:
            print(_name.text)
            if restaurant in _name.text:
                name = _name.text
                break

        # click on restaurant and navigate to menu page
        #time.sleep(2)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, name)))
        link = driver.find_element(By.LINK_TEXT, name)
        driver.execute_script('arguments[0].click()', link)

        time.sleep(3)

        # Try to find the search bar- if it cannot be accessed, go back to close the popup
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "search-suggestions-typeahead-input")))
            test = driver.find_element(By.ID, "search-suggestions-typeahead-input")
            test.send_keys(Keys.CONTROL + "a")
        except:
            driver.back()

        # Get the correct xpath
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[5]/div[1]/div[4]/ul/li')))
            xpath = '//*[@id="main-content"]/div[5]/div[1]/div[4]/ul/li'
        except:
            xpath = '//*[@id="main-content"]/div[6]/div[1]/div[4]/ul/li'

        # Obtain list of items from menu and process
        #time.sleep(5)
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
            items = driver.find_elements(By.XPATH, xpath) 
        except:
            driver.back()
            continue
        # Look for cheapest option, add cheapest to dictionary
        # Cycle through categories of menu
        for category in items:
            try:
                category_name = category.find_element(By.TAG_NAME, 'h3')
                #print("----Category: " + category_name.text)

                # Get menu items and information
                WebDriverWait(category, 10).until(EC.presence_of_element_located((By.XPATH, './ul')))
                #time.sleep(1)
                menu_list = category.find_element(By.XPATH, './ul')

                WebDriverWait(menu_list, 10).until(EC.presence_of_element_located((By.XPATH, './li')))
                #time.sleep(1)
                menu_items = menu_list.find_elements(By.XPATH, './li')

                for menu_item in menu_items:
                    try:
                        data = re.split('\n|•', menu_item.text)
                        if data[0] == "Popular":
                            item_name = data[1]
                            item_price = data[2]
                        else:
                            item_name = data[0]
                            item_price = data[1]
                        # remove dollar sign
                        item_price = item_price[1:]
                        # If category contains keywords
                        #print(item_name + " " + item_price)
                        if item.lower() in category_name.text.lower():
                            # if restaurant has not been added or new product is cheaper
                            if restaurant not in scraped_products or scraped_products[restaurant][1] > float(item_price):
                                scraped_products[restaurant] = (item_name, float(item_price))
                        # If itemname contains keywords
                        elif item.lower() in item_name.lower():
                            if restaurant not in scraped_products or scraped_products[restaurant][1] > float(item_price):
                                scraped_products[restaurant] = (item_name, float(item_price))
                    except Exception as e:
                        #print(e)
                        #print("No data in this menu entry")
                        pass
            except:
                # gap in the menu- skip over since no data is displayed in element block
                #print("No data in this category")
                pass

        # Navigate back to list of restaurants
        time.sleep(1)
        driver.back()
        time.sleep(1)

    return scraped_products

# address = "125 Spence St, College Station" #Zachry Engineering Building
# item = "Matcha"
# stores = ["Starbucks", "Sharetea"]
# results = uberEats(stores, item, address)
# print("Results:")
# print(results)