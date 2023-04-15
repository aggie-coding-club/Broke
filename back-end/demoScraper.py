from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def demo():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.tamu.edu/")

    driver.maximize_window()

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

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "ctl00_ContentPlaceHolder1__editor__pageContent"))
        )

        paragraphs = element.find_elements(By.TAG_NAME, 'p')
        
        info = dict()

        for idx, p in enumerate(paragraphs[:5]):
            info[idx] = p.text.strip()
        
        driver.quit()

        return info

    except:
        driver.quit()
        return None

