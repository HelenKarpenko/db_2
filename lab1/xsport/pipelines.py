# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from lxml import etree


class XsportPipeline(object):
    def open_spider(self, spider):
        self.root = etree.Element('data')

    def close_spider(self, spider):
        with open('results/xsport.xml', 'wb') as file:
            etree.ElementTree(self.root).write(file, pretty_print=True, encoding="UTF-8")

    def process_item(self, item, spider):
        page = etree.SubElement(self.root, 'page', url=item['url'])
        for text in item['text']:
            etree.SubElement(page, 'fragment', type='text').text = text
        for url in item['images']:
            etree.SubElement(page, 'fragment', type='image').text = url
        return item
