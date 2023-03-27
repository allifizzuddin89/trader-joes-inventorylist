# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# MYSQL database setup
import mysql.connector
from mysql.connector import errorcode
from scrapy.exceptions import DropItem

class TraderJoesInventoryPipeline:
    def __init__(self, host, user, password, database, table):
        self.host = 'localhost',
        self.user = 'traderjoes',
        self.password = '1234567890',
        self.database = 'traderjoesinventory'
        self.table = 'quotes'
        # self.port = '3306'

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_PASSWORD'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            table=crawler.settings.get('MYSQL_TABLE')
        )

    def open_spider(self, spider):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

        # Check if table exists
        self.cursor.execute(f"SHOW TABLES LIKE '{self.table}'")
        if not self.cursor.fetchone():
            # Create table
            self.cursor.execute(f'''
                CREATE TABLE {self.table} (
                    Item_Name VARCHAR(255), 
                    Main_Category VARCHAR(255),
                    Sub_Category VARCHAR(255),
                    Sub_Sub_Category VARCHAR(255),
                    Price int,
                    Packaging_Size int,
                    Size_Unit VARCHAR(255),
                    SKU int,
                    PRIMARY KEY (Item_Name)
                )
            ''')
            self.conn.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(f'''
                INSERT INTO {self.table} 
                (Item_Name, Main_Category, Sub_Category, Sub_Sub_Category, Price, Packaging_Size, Size_Unit, SKU) 
                VALUES 
                (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (item['Item_Name'], item['Main_Category'], item['Sub_Category'], item['Sub_Sub_Category'], item['Price'], item['Packaging_Size'], item['Size_Unit'],item['SKU']))

            self.conn.commit()
            return item
        except mysql.connector.Error as e:
            raise DropItem(f'Error inserting item: {e}')

class SavingToMysqlPipeline(object):
    def __init__(self):
        self.create_connection()
    
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



# class TraderJoesInventoryPipeline:
        # def process_item(self, item, spider):
        #         # print('PIPELINE : {}'.format(item['Item_Name']))
        #         return item


    # Configure database pipeline inside _init_
    # def __init__(self):
    #     self.conn = mysql.connector.connect(
    #         host = 'localhost',
    #         user = 'traderjoes',
    #         password = '1234567890',
    #         database = 'traderjoesinventory',
    #         port = '3306'
    #     )

    #     ## Create cursor, used to execute commands
    #     self.cur = self.connection.cursor()
        
    #     ## Create quotes table if none exists
    #     self.cur.execute("""
    #     CREATE TABLE IF NOT EXISTS quotes(
    #         Item_Name VARCHAR(255), 
    #         Main_Category VARCHAR(255),
    #         Sub_Category VARCHAR(255),
    #         Sub_Sub_Category VARCHAR(255),
    #         Price int,
    #         Packaging_Size int,
    #         Size_Unit VARCHAR(255),
    #         SKU int,
    #         PRIMARY KEY (Item_Name)
    #     )
    #     """)
       
    # # store the data inside mysql database
    # def process_item(self, item, spider):        
    #      ## Define insert statement
    #     self.cur.execute(""" insert into quotes (Item_Name, Main_Category, Sub_Category, Sub_Sub_Category, Price, Packaging_Size, Size_Unit, SKU ) values (%s,%s,%s,%s,%s,%s,%s,%s)""", (
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
