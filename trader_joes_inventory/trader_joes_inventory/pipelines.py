# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# MYSQL database setup
import mysql.connector


class TraderJoesInventoryPipeline:
        def process_item(self, item, spider):
                # print('PIPELINE : {}'.format(item['Item_Name']))
                return item
    # # Configure database pipeline inside _init_
    # def __init__(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'traderjoes',
    #         password = '1234567890',
    #         database = 'traderjoesinventory'
            # port = '3306'
        # )

        # ## Create cursor, used to execute commands
        # self.cur = self.conn.cursor()
        
        # ## Create quotes table if none exists
        # self.cur.execute("""
        # CREATE TABLE IF NOT EXISTS quotes(
        #     Item_Name VARCHAR(255), 
        #     Main_Category VARCHAR(255),
        #     Sub_Category VARCHAR(255),
        #     Sub_Sub_Category VARCHAR(255),
        #     Price int,
        #     Packaging_Size int,
        #     Size_Unit VARCHAR(255),
        #     SKU int,
        #     PRIMARY KEY (Item_Name)
        # )
        # """)
       
    # # store the data inside mysql database
    # def process_item(self, item, spider):        
    #      ## Define insert statement
    #     self.cur.execute(""" insert into (Item_Name, Main_Category, Sub_Category, Sub_Sub_Category, Price, Packaging_Size, Size_Unit, SKU ) values (%s,%s,%s,%s,%s,%s,%s,%s)""", (
    #         item["Item_Name"],
    #         item["Main_Category"],
    #         item["Sub_Category"],
    #         item["Sub_Sub_Category"],
    #         item["Price"],
    #         item["Packaging_Size"],
    #         item["Size_Unit"],
    #         item["SKU"],
    #     ))

    #     ## Execute insert of data into database
    #     self.conn.commit()
    #     return item

    # # avoid duplicate item
    # def process_item(self, item, spider):

    #     ## Check to see if text is already in database 
    #     self.cur.execute("select * from quotes where content = %s", (item['Item_Name'],))
    #     result = self.cur.fetchone()

    #     ## If it is in DB, create log message
    #     if result:
    #         spider.logger.warn("Item already in database: %s" % item['text'])

    #     ## If text isn't in the DB, insert data
    #     else:
    #         ## Define insert statement
    #         self.cur.execute(""" insert into (Item_Name, Main_Category, Sub_Category, Sub_Sub_Category, Price, Packaging_Size, Size_Unit, SKU ) values (%s,%s,%s,%s,%s,%s,%s,%s)""", (
    #         item["Item_Name"],
    #         item["Main_Category"],
    #         item["Sub_Category"],
    #         item["Sub_Sub_Category"],
    #         item["Price"],
    #         item["Packaging_Size"],
    #         item["Size_Unit"],
    #         item["SKU"],
    #     ))
    #     ## Execute insert of data into database
    #     self.conn.commit()
    #     return item

    
    # def close_spider(self, spider):

    #     ## Close cursor & connection to database 
    #     self.cur.close()
    #     self.conn.close()

# class SavingToMysqlPipeline(self,object):
#         def __init__(self):
#         self.create_connection()