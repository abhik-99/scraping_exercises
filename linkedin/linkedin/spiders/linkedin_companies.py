# -*- coding: utf-8 -*-
import scrapy


class LinkedinCompaniesSpider(scrapy.Spider):
    name = 'linkedin_companies'
    allowed_domains = ['www.linkedin.com']
    start_urls = ['http://www.linkedin.com/']

    def parse(self, response):
        pass
