from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tutorial.items import RinkItem

class Arenas(CrawlSpider):
    name = 'arenas'
    allowed_domains = ['arenamaps.com']
    start_urls = ['http://arenamaps.com/arenas/']
    
    rules = (
        Rule(SgmlLinkExtractor(allow=("arenas/(\D+)\.htm"), process_value=lambda s: s.replace('&#xA;', '').strip(), ), follow=True),
        Rule(SgmlLinkExtractor(allow=("arenas/(\d+)(.*)"), process_value=lambda s: s.replace('&#xA;', '').strip(), ), callback='parse_rink', follow=True),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)

    def parse_rink(self, response):
        address = response.xpath('//div[@id="arena_addr"]')
        item = RinkItem()
        
        item["title"] = address.xpath('./font//text()').extract()[0];

        text = address.xpath('./text()').extract();
        item["address"] = text[0];
        item["address2"] = text[1];
        item["phone"] = text[2];
        item["whole_address"] = text
        return item;