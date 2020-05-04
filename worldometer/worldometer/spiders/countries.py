# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometer.info']
    start_urls = ['https://www.worldometer.info/']

    def parse(self, response):
        pass
