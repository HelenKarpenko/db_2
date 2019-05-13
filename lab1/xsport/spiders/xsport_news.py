# -*- coding: utf-8 -*-
import scrapy


class XsportNewsSpider(scrapy.Spider):
    name = 'xsport_news'
    start_urls = ['https://xsport.ua/news/']
    custom_settings = {
        'ITEM_PIPELINES': {
            'xsport.pipelines.XsportPipeline': 300,
        }
    }

    def parse(self, response):
        for text in response.xpath("//div[@class='detail-text-holder']"):
            yield {
                'url': response.url,
                'text': text.xpath(".//p/text()").extract(),
                'images': text.xpath(".//img/@src").extract(),
            }

        for a in response.xpath("//div[@class='standard-news-list']").xpath(".//a[@class='blue-icons-hover']/@href"):
            yield response.follow(a.extract(), callback=self.parse)
