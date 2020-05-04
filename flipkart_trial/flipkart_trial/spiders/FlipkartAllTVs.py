# -*- coding: utf-8 -*-
import scrapy


class FlipkartalltvsSpider(scrapy.Spider):
    name = 'FlipkartAllTVs'
    start_urls = ['https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&page=1']

    def parse(self, response):
        print('Starting', response)
        for eachTv in response.xpath('//div[@class="_1-2Iqu row"]'):
            yield {
                "tv_name": eachTv.xpath('.//div[1]/div[@class="_3wU53n"]/text()').get(),
                "original_price": eachTv.xpath('.//div[2]/div[1]/div[1]/div[1]/text()').get(),
                "discounted_price": eachTv.xpath('.//div[2]/div[1]/div[1]/div[2]/text()[2]').get(),
                "discount_percent": eachTv.xpath('.//div[2]/div[1]/div[1]/div[3]/span/text()').get(),
                "rating": eachTv.xpath('.//div[1]/div[2]/span/div[1]/text()').get(),
                "internet_features": eachTv.xpath('.//div[1]/div[3]/ul/li[1]/text()').get(),
                "operating_system": eachTv.xpath('.//div[1]/div[3]/ul/li[contains(text(), "Operating System")]/text()').get(),
                "resolution": eachTv.xpath('.//div[1]/div[3]/ul/li[contains(text(), "Pixels")]/text()').get(),
                "hdmi": eachTv.xpath('.//div[1]/div[3]/ul/li[contains(text(), "HDMI")]/text()').get(),
                "usb": eachTv.xpath('.//div[1]/div[3]/ul/li[contains(text(), "USB")]/text()').get(),
            }
        nextPage ="https://www.flipkart.com" + response.xpath('//a/span[contains(text(), "Next")]/ancestor:: node()[1]/@href').get()
        
        print("\n\nNext Page", nextPage, "\n\n")

        if nextPage:
            yield response.follow(url = nextPage, callback = self.parse)
        

