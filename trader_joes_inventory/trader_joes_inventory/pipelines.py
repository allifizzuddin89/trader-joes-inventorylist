# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
# MYSQL database setup
import mysql.connector
from mysql.connector import errorcode
from scrapy.exceptions import DropItem

class SavingToMysqlPipeline(object):
    def __init__(self):
        self.create_connection()
    
    # please setup your own MYSQL database
    # below details such as host, user, password, database, port
    # definitely not working on your machine
    # please refer https://dev.mysql.com/doc/mysql-getting-started/en/
    # to setup your own MYSQL database, table
    def create_connection(self):
        self.connection =mysql.connector.connect(
            host = 'localhost',
            user = 'traderjoes',
            password = '1234567890',
            database = 'traderjoesinventory',
            # table = 'quotes',
            port = '3306'
        )
        ## Create cursor, used to execute commands
        self.curr = self.connection.cursor()
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        # insert ignore into or replace into
        # this is important on handling duplicate data
        self.curr.execute(""" replace into quotes (Item_Name, Main_Category, Sub_Category, Sub_Sub_Category, Price, Currency, Packaging_Size, Size_Unit, SKU) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
            item["Item_Name"],
            item["Main_Category"],
            item["Sub_Category"],
            item["Sub_Sub_Category"],
            item["Price"],
            item["Currency"],
            item["Packaging_Size"],
            item["Size_Unit"],
            item["SKU"],
        ))
        self.connection.commit()