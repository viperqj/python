# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_num = scrapy.Field()
    p_title=scrapy.Field()
class DetailItem(scrapy.Item):
    p_content = scrapy.Field()
    p_id =scrapy.Field()