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

target_url = "https://losangeles.craigslist.org/sitemap/index.xml"

driver.get(target_url)

folders = driver.find_elements(By.CLASS_NAME, "folder")

links = []
links_2 = []
results = []

for i in range(1, len(folders)):
    folder = folders[i-1]
    opened = folder.find_element(By.CLASS_NAME, "opened")
    line = opened.find_element(By.CLASS_NAME, "line")
    url = line.find_elements(By.TAG_NAME, "span")[1].text
    links.append(url)
print("links", links)

for i in range (1, len(links)):
    driver.get(links[i])
    folders_2 = driver.find_elements(By.CLASS_NAME, "folder")

    for i in range(1, len(folders_2)):
        folder = folders_2[i]
        opened = folder.find_element(By.CLASS_NAME, "opened")
        line = opened.find_element(By.CLASS_NAME, "line")
        url = line.find_elements(By.TAG_NAME, "span")[1].text
        links_2.append(url)

for i in range (1, len(links_2)):
    driver.get(links_2[i-1])
    # driver.get("https://losangeles.craigslist.org/search/acc")
    search_page = driver.find_element(By.ID, "search-results-page-1")
    ol_element = search_page.find_element(By.TAG_NAME, "ol")
    time.sleep(5)
    lists = ol_element.find_elements(By.TAG_NAME, "li")
    for i in range(1, len(lists)):
        li_element = lists[i]
        result = li_element.find_element(By.TAG_NAME, "a").get_attribute("href")
        results.append(result)

print("results", results)

driver.close()
driver.quit()