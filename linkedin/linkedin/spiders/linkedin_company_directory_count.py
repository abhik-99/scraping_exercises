# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
XPath for-
Number of companies starting with the same alpahbet - //*[@id="seo-dir"]/div/div[4]/div/ol/li

"""
class LinkedinCompanyDirectoryCountSpider(CrawlSpider):
    name = 'linkedin_company_directory_count'
    allowed_domains = ['www.linkedin.com/directory/companies']
    start_urls = ['https://www.linkedin.com/directory/companies/a']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= '//*[@id="seo-dir"]/div/div[2]/div/ol/li/a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print("Number of Companies at",response.url,"is",len(response.XPath('//*[@id="seo-dir"]/div/div[4]/div/ol/li')))
