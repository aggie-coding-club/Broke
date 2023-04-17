from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

number_of_stores = 25

def googleMap(item : str, address: str) -> dict : 
    
    '''
    Locate search bar
    Enter address, hit enter
    Enter item, hit enter
    Check $ checkbox
    Grab top <twenty five> titles of places
    This threshold will be a variable so we can easily change it
    Don’t include the same place twice (like McDonald)
    Return a dictionary of names and address
    {“McDonald” : “801 university dr, college station, tx”}, {“Hopdoddy” : “...”}, …
    '''
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
    action = webdriver.ActionChains(driver)
    driver.get("https://www.google.com/maps")
    driver.maximize_window()
    
    time.sleep(2)

    # Search Location
    searchBox = driver.find_element(By.ID, "searchboxinput")
    searchBox.clear()
    searchBox.send_keys(address)
    searchBox.send_keys(Keys.RETURN)
    
    time.sleep(1)
    
    # Search Item
    searchBox.clear()
    searchBox.send_keys(item)
    searchBox.send_keys(Keys.RETURN)
    
    time.sleep(3)
    
    # Scroll Window to Load Results
    results_window = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]')

    # Scroll down 3 times, will have to be changed if we edit number of stores, it should probably be something like Math.Ceil(NumberOfStores / 25 * 3)
    for i in range(3):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', results_window)
        time.sleep(2)

    
    results = {}

    # Exception here because there are not enough stores in normal response
    for i in range(3,number_of_stores*2 + 3,2): 
        try:
            location_name = f"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{i}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]"
            namebox = driver.find_element(By.XPATH, str(location_name))
        
            name = namebox.text

            address_loc = f"/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{i}]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/span[2]"
            addressbox = driver.find_element(By.XPATH, str(address_loc))
            
            address = addressbox.text
            
            results[name] = address
        except:
            print("Out of Results")
            break

    
    driver.quit()
    
    return results

from geopy import Nominatim
from geopy import distance

def filterAddress(address : str) -> str:
    '''
    get rid of the unit and building address in the address
    '''
    unit_result = 'unit' in address.lower()
    building_result = 'building' in address.lower()
    suite_result = 'suite' in address.lower()
    if unit_result:
        unit_index = address.lower().index('unit')
        #space_index = address.lower().index(' ', unit_index) + 1
        #city_index = address.lower().index(' ', space_index)
        return address[0: unit_index] #+ address[city_index:]
    elif building_result:
        building_index = address.lower().index('building')
        #space_index = address.lower().index(' ', building_index) + 1
        #city_index = address.lower().index(' ', space_index)
        return address[0: building_index] #+ address[city_index:]
    elif suite_result:
        suite_index = address.lower().index('suite')
        #space_index = address.lower().index(' ', suite_index) + 1
        #city_index = address.lower().index(' ', space_index)
        return address[0: suite_index]##+ address[city_index:]
    return address


def distanceFunct(list_of_stores : dict, radius : int, address : str) -> dict:

    '''
    Filter out list of restaurants within the radius specified by the user 
    Return dictionary of qualified restaurants
    '''
    filtered_stores = {}
    g = Nominatim(user_agent="Broke")
    
    _, addr = g.geocode(address)

    address = filterAddress(address)

    print(address)
    
    for store in list_of_stores:
        store_address = filterAddress(list_of_stores[store])
        print('store', store_address)
        try:
            _, dic = g.geocode(store_address)
        except:
            continue
        d = distance.distance(dic, addr).miles
        if d <= radius:
            filtered_stores.update({store : store_address})
    

    return filtered_stores

# ''' for checking purposes '''
# list_of_stores = {'McDonalds' : '801 University Dr College Station, Texas', 'Home' : '801 Luther St W, Unit 1102, College Station, Texas', 'Star Cinema Grill' : '1037 University Dr, College Station, Texas'}
# filtered_stores = distanceFunct(list_of_stores, 2, '125 Spence St, College Station, Texas')
# for store in filtered_stores:
#         print(store + " : " + filtered_stores[store])

# print(googleMap('burger', '2604 Zambia Drive, Cedar Park'))
