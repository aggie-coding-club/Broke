
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


def gasSearch(input: str, address: str) -> list:

    '''
    take 2 parameters, type_of_gas specifiying regular or diesel, and radius
    '''

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
    driver.get("https://www.gasbuddy.com/home")
    driver.maximize_window()

    # Search location
    location = driver.find_element(By.ID, "search")
    location.clear()
    location.send_keys(address)
    location.send_keys(Keys.RETURN)

    # edit link and reload if diesel
    if input == "diesel":
        link = driver.current_url
        fuel_type_index = link.index("fuel") + 5
        newlink = link[:fuel_type_index] + "4" + link[fuel_type_index+1:]
        driver.get(newlink)

    try:
        # Load more results- first time
        time.sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/a')
        driver.execute_script("arguments[0].click();", button)
        
        # Load more results- subsequent times
        # Needs to wait for previous process to finish or else results will be duplicated
        # If need more results, copy and paste the following four lines of code 
        driver.implicitly_wait(5)
        time.sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/a')
        driver.execute_script("arguments[0].click();", button)

        # Load more- subsequent time
        driver.implicitly_wait(5)
        time.sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/a')
        driver.execute_script("arguments[0].click();", button)

    except Exception as e:
        print(e)
        driver.quit()
    

    # Obtain gas stations list
    time.sleep(5)
    stations = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[1]/div[3]/div')

    station_list = []

    for station in stations:
        elements = station.text.split("\n")
        # first element is the name
        name = elements[0] 
        # third element is the address
        address = elements[3]
        # fifth element is the price
        price = elements[5]

        # name sometimes takes up 2 indices, so shift address and price if that occurs
        if elements[1][0:2] == "& ":
            address = elements[4]
            price = elements[6]

        # do not add to list if price is not given
        if '$' not in price:
            continue
        
        # add to list
        station_list.append([name, address, price])

        print(name + " " + address + " " + price)


    return station_list


gas = gasSearch("diesel", "Bronx")

