import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from WikiScraper.items import WikiscraperItem



class CrawlSpider(CrawlSpider):
    name = 'crawl'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['http://en.wikipedia.org/wiki/LeBron_James']
    key = 0

    #create a list of rules for the crawler to follow
    #call back is the function it should call to parse each link
    #follow denotes if it should depth first search into new link it finds on each page
    #link extractor states which link we can go to with an r expression
    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse', follow=True)]

    def parse(self, response):

        """
        return{
            "URL" : response.url,
            "Player" : response.xpath('//h1[@id="firstHeading"]/text()').get(),
            "LastEdited" : response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        }
        """
        item = WikiscraperItem()
        #since we are using item object we will be returning that after we populate its properties
        self.key += 1

        item['key'] = self.key
        item['url'] = response.url
        item['name'] = response.xpath('//h1[@id="firstHeading"]/text()').get()
        item['lastupdated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()

        return item
