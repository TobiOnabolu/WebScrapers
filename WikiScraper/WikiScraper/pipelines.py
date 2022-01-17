# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


#pipelines used for cleaning your item data records after scraping 
#makes it easier than doing seperate cleaning for each crawler
class WikiscraperPipeline:
    def process_item(self, item, spider):
        #spider.logger.info('A response from just arrived!')

        #drop item if one of the fields is missing
        if not item['lastupdated'] or not item['url'] or not item['name'] or not item['league']:
            raise DropItem("Missing Field") #from scrapy, used to drop a record


        return item
#have seperate pipeline classes for each specific thing u want to do
