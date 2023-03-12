import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()) )
driver.get("https://www.tamu.edu/")

# print out the title of the page
print(driver.title)

# ID -> Class -> name
search = driver.find_element(By.ID, "searchfield")
# clears the field so we are not appending to pre-existant text
search.clear()
search.send_keys("aggie ring")
search.send_keys(Keys.RETURN)

try:
    # explicit wait
    # wait up to 10 seconds until the presence of linker text "Aggie Ring" is found
    # purpose is to ensure the locating of elements in situations of delays of website loading
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Aggie Ring"))
    )
    link.click()
    
    # allows time to pause for 5 seconds, extending the pop up time of the chrome tab
    time.sleep(5)
    print(driver.title) 

    element = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1__editor__pageContent")
    #print(element.text)

    paragraphs = element.find_elements(By.TAG_NAME, 'p')
    for p in paragraphs[:5]:
        print(p.text)
        print()

    '''
    # allows you to go back to the previous page
    driver.back()
    driver.back()
    # allows you to move forward to the page you went back on
    driver.forward()
    time.sleep(5)
    '''

except:
    driver.quit()

