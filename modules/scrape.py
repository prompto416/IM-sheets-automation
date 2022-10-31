

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup 

def scrapeHTML_string():
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    s=Service(PATH)
    options = webdriver.ChromeOptions() 
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.headless = True
    driver = webdriver.Chrome(options=options, service=s)
    url = ("https://www.set.or.th/th/tch/rules-regulations/regulations?fbclid=IwAR06NR4BDsK_1Sl-6QzyzHHuW-sHpgbE8uo6dtF0qGx6Udwo1eolYEvHnRM#noti-margin-rate-2022")
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    time.sleep(3)
    elements = soup.find(class_="rules-books-render-recursive")
    time.sleep(3)


    elements_string = str(elements)

    if len(elements_string) > 100:
        # f = open('cacheDebug.txt','w')
        # f.write(elements_string)
        # f.close()
        # print('finished writing file')
        return elements_string
    else:
        print('Error: None Type Detected!')
        return None


    driver.quit()
    
