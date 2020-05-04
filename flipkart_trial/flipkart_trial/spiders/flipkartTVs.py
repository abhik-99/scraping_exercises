# -*- coding: utf-8 -*-
import scrapy


class FlipkarttvsSpider(scrapy.Spider):
    name = 'flipkartTVs'
    allowed_domains = ['www.flipkart.com/televisions/pr?sid=ckf%2Cczl']
    start_urls = ['http://www.flipkart.com/televisions/pr?sid=ckf%2Cczl/']

    def parse(self, response):
        for eachTv in response.xpath('//div[@class="_1-2Iqu row"]'):
            yield {
                "tv_name": eachTv.xpath('.//div[1]/div[@class="_3wU53n"]/text()').get(),
                "original_price": eachTv.xpath('.//div[2]/div[1]/div[1]/div[1]/text()').get(),
                "discounted_price": eachTv.xpath('.//div[2]/div[1]/div[1]/div[2]/text()').get(),
                "discount_percent": eachTv.xpath('.//div[2]/div[1]/div[1]/div[3]/span/text()').get(),
                "rating": eachTv.xpath('.//div[1]/div[2]/span/div[1]/text()').get()
            }
