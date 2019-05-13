import scrapy


class MebliumSpider(scrapy.Spider):
    name = 'meblium'
    start_urls = ['https://www.meblium.com.ua/myagkaya-mebel/divany/']
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }

    def parse(self, response):
        for product in response.xpath('//div[@id="category-products"]//div[contains(@class,"product in_action")]'):
            yield {
                'title': product.xpath('.//div[@class="product-info"]/span[@class="product-name"]/text()').extract(),
                'price': product.xpath('.//a[contains(@class,"buy-button")]/text()').get().strip(),
                'img': product.xpath('.//span[@class="product-image"]/img/@src').get(),
            }

        for a in response.xpath('//div[@id="pagination"]//span/a/@href'):
            yield response.follow(a.extract(), callback=self.parse)
