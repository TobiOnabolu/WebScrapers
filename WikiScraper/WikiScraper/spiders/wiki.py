import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['Wikipedia.org']
    start_urls = ['http://Wikipedia.org/wiki/LeBron_James']

    def parse(self, response):

        #// allows to select an h1 anywhere in the DOM
        #//div/h1 allows to select h1 following any div in the dom
        #@ goes b4 attributes and u specify what the attribute should equal
        # the last / is what u are collecting
        title = response.xpath('//h1[@id="firstHeading"]/text()').get()
        
        #Xpath selector work similiar to SQl where they select all the records that match ur call
        #To go down the chain of a dm using / , they need to be descendants of eachother. Which is why th didnt work to call tr
        position = response.xpath('//tr/td/a[@href="/wiki/Small_forward"]/text()').get()
        return {
            "Name" : title, 
            "Positon" : position}
