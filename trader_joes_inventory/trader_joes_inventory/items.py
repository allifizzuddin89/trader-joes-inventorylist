# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import item loader
# data cleaning with item loader processor
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


# setup pipeline
# from scrapy.Item import Item, Field


# class TraderJoesInventoryItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

# def remove_currency(value):
#     return value.replace("USD",'').strip()

class TraderJoesInventoryItem(scrapy.Item):
    Item_Name = scrapy.Field()
    Main_Category = scrapy.Field()
    Sub_Category = scrapy.Field()
    Sub_Sub_Category = scrapy.Field()
    Price = scrapy.Field()
    Currency = scrapy.Field()
    Packaging_Size = scrapy.Field()
    Size_Unit = scrapy.Field()
    SKU = scrapy.Field()

    ## If using css or xpath selector and needs cleaning
    ## In this case, we use api request, so mehhhhh ignore below
    # Item_Name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Main_Category = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Sub_Category = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Sub_Sub_Category = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Price = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Currency =scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency), output_processor = TakeFirst())
    # Packaging_Size = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # Size_Unit = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
    # SKU = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor = TakeFirst())
