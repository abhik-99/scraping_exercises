# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FlipkartmobilesSpider(CrawlSpider):
    name = 'flipkartMobiles'
    allowed_domains = ['www.flipkart.com']
    start_urls = ['https://www.flipkart.com/search?sid=tyy&page=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="_1HmYoV _35HD7C"]/div/div/div/div/a[@class="Zhf2z-"]'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[@class = "_3fVaIS"]/span[contains(text(), "Next")]/..'))
    )

    def parse_item(self, response):
        yield {
            'product_name': response.xpath('//span[@class="_35KyD6"]/text()').get(),
            'ram': response.xpath('//div[@class = "_3WHvuP"]/ul/li[contains(text(), "RAM")]/text()').get(),
            'rom': response.xpath('//div[@class = "_3WHvuP"]/ul/li[contains(text(), "ROM")]/text()').get(),
            'display': response.xpath('//div[@class = "_3WHvuP"]/ul/li[contains(text(), "inch") and contains(text(), "Display")]/text()').get(),
            'battery': response.xpath('//div[@class = "_3WHvuP"]/ul/li[contains(text(), "Battery")]/text()').get(),
            'processor': response.xpath('//div[@class = "_3WHvuP"]/ul/li[contains(text(), "Processor")]/text()').get(),
            'sim_type': response.xpath('//td[@class="_3-wDH3 col col-3-12" and contains(text(), "SIM Type")]/../td[2]/ul/li/text()').get(),
            'discounted_price': response.xpath('//div[@class="_1uv9Cb"]/div[@class = "_1vC4OE _3qQ9m1"]/text()').get(),
            'actual_price': response.xpath('//div[@class="_1uv9Cb"]/div[@class = "_3auQ3N _1POkHg"]/text()[2]').get()
        }
