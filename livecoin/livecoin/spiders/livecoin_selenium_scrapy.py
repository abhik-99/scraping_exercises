# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.chrome.options import Options
from shutil import which 

class LivecoinSeleniumScrapySpider(scrapy.Spider):
    name = 'livecoin_selenium_scrapy'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = [
        'https://www.livecoin.net/en'
    ]

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_path = which("chromedriver")

        driver = webdriver.Chrome(executable_path= chrome_path,
        options= chrome_options)
        driver.get("https://www.livecoin.net/en")
        driver.set_window_size(1920, 1080)
        usd_tab = driver.find_element_by_xpath('//div[contains(@class,"filterPanelItem___2z5Gb ")][3]')
        usd_tab.click()
        self.html = driver.page_source
        driver.close()

    def parse(self, response):
        resp = Selector(text = self.html)
        for eachCurrecy in resp.xpath('//div[contains(@class," tableRow___3EtiS ")]'):
            yield {
                'currency_pair': eachCurrecy.xpath('.//div[1]/div/text()').get(),
                'volume': eachCurrecy.xpath('.//div[2]/span/text()').get(),
                'last_price': eachCurrecy.xpath('.//div[3]/span/text()').get()
            }            
