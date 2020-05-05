# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ImdbbestmoviesSpider(CrawlSpider):
    name = 'ImdbBestMovies'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/list/ls068082370/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = (r'//h3[@class="lister-item-header"]/a')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath('.//div[@class = "title_wrapper"]/h1/text()').get(),
            'year': response.xpath('.//div[@class = "title_wrapper"]/h1/span/a/text()').get(),
            'director': response.xpath('.//div[@class="plot_summary "]/div[@class="credit_summary_item"]/h4[contains(text(),"Director")]/../a/text()').get(),
            'rating': response.xpath('.//span[@itemprop="ratingValue"]/text()').get(),
            'running_time': response.xpath('normalize-space(.//div[@class = "title_wrapper"]/div/time/text())').get(),
            'genre_1': response.xpath('.//div[@class = "title_wrapper"]/div/a[1]/text()').get(),
            'genre_2': response.xpath('.//div[@class = "title_wrapper"]/div/a[2]/text()').get(),
        }
