import os
import time
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
import csv
import json

options = Options()

options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-web-security")
options.add_argument("--disable-content-safety-policy")
options.add_argument("--disable-features=CrossSiteDocumentBlockingIfIsolating")
options.add_argument('disable-infobars')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("prefs", {"download.prompt_for_download": False})
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-javascript")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(options=options, service=service)

target_url = "https://losangeles.craigslist.org/sitemap/index-by-date-cat.xml"
# target_url = "https://losangeles.craigslist.org/sitemap/index.xml"

driver.get(target_url)

folders = driver.find_elements(By.CLASS_NAME, "folder")

links = []
links_2 = []

for i in range(1, len(folders)):
    folder = folders[i-1]
    opened = folder.find_element(By.CLASS_NAME, "opened")
    line = opened.find_element(By.CLASS_NAME, "line")
    url = line.find_elements(By.TAG_NAME, "span")[1].text
    links.append(url)

for i in range (1, len(links)):
    driver.get(links[i])
    folders_2 = driver.find_elements(By.CLASS_NAME, "folder")
    print("folder_2 number", len(folders_2))

    for i in range(1, len(folders_2)):
        folder = folders_2[i]
        opened = folder.find_element(By.CLASS_NAME, "opened")
        line = opened.find_element(By.CLASS_NAME, "line")
        url = line.find_elements(By.TAG_NAME, "span")[1].text
        links_2.append(url)

print("links_2", links_2)



driver.close()
driver.quit()