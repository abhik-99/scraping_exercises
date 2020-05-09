"""
Create a "credentials.json" in this directory and use the keys
Username - for your username
Password - for your password
Search - the item to search
before running this script.
"""



from selenium import webdriver
from shutil import which
from selenium.webdriver.chrome.options import Options
import time
import json

with open("credentials.json", 'r') as fp:
    credentials = json.load(fp)

chrome_path = which("chromedriver")

driver = webdriver.Chrome(chrome_path)
driver.get('https://www.linkedin.com/login?')
time.sleep(2)
username_input = driver.find_element_by_xpath('//*[@id="username"]')
username_input
username_input.send_keys(credentials['Username'])

password_input = driver.find_element_by_xpath('//*[@id="password"]')
password_input.send_keys(f'{credentials["Password"]}\n')
time.sleep(2)

search_bar = driver.find_element_by_xpath('//input[contains(@class, "search-global-typeahead__input always-show-placeholder")]')
search_bar.send_keys(f"{credentials['Search']}\n")
print(driver.current_url)
time.sleep(15*60)

driver.close()