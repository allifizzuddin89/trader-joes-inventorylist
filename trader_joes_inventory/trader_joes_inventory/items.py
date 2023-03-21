# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# setup pipeline
# from scrapy.Item import Item, Field


# class TraderJoesInventoryItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class TraderJoesInventoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Item_Name = scrapy.Field()
    Main_Category = scrapy.Field()
    Sub_Category = scrapy.Field()
    Sub_Sub_Category = scrapy.Field()
    Price = scrapy.Field()
    Packaging_Size = scrapy.Field()
    Size_Unit = scrapy.Field()
    SKU = scrapy.Field()
