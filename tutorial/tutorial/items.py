# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RinkItem(scrapy.Item):
	title = scrapy.Field()
	title2 = scrapy.Field()
	address = scrapy.Field()
	address2 = scrapy.Field()
	phone = scrapy.Field()
	whole_address = scrapy.Field()