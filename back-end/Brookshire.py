from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# IGNORE THIS- TUTORIAL FOR SCRAPING

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )

# Navigate to site
driver.get("https://shop.brookshirebrothers.com/brookshire_brothers_12")


time.sleep(10)

# Find the search bar and enter a search term
search_bar = driver.find_element(By.XPATH,'/html/body/rosie-root/rosie-shell/rosieui-layout/main/div[1]/rosie-header/rosieui-header-layout/div/div/div/rosieui-header-section[2]/div/rosie-search-typeahead/div/div/div/input')
search_bar.send_keys("Apples")

# Submit the search and wait for the page to load
search_bar.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
time.sleep(15)


# Find the price of the item and print it
names = driver.find_elements(By.CLASS_NAME, "name")
prices = driver.find_elements(By.CLASS_NAME, "description")
for i in range(len(names)):
    print(names[i].text)
    print(prices[i].text)

# Close the driver
driver.quit()
