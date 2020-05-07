from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_path = which("chromedriver")

driver = webdriver.Chrome( executable_path = chrome_path, options = chrome_options)

driver.get("https://duckduckgo.com")
search_box = driver.find_element_by_xpath('(//input[@id=\"search_form_input_homepage\"])[1]')
search_box.send_keys("My User Agent")
search_box.send_keys(Keys.ENTER)
print(driver.page_source)
driver.close()