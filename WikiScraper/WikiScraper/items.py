# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#When you have multiple crawlers each with their own website
#their parse function wont be the same
#but their data returned will be the same
#so to group all that data returned, regardless where it came from, we use items


class WikiscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    lastupdated = scrapy.Field()
    name = scrapy.Field()
    key = scrapy.Field()
    league = scrapy.Field()

