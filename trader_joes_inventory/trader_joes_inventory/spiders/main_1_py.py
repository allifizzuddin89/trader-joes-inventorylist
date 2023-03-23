import scrapy
import os
import sys

ROOT_DIR = os.path.abspath(os.curdir)

# sys.path.append(ROOT_DIR)
# sys.path.append(ROOT_DIR+"/trader-joes-inventorylist/trader_joes_inventory/trader_joes_inventory/")
sys.path.insert(0,"/home/allifizzuddin/Documents/Freelance_ job/Job_2023/trader-joes-list/trader-joes-inventorylist/trader_joes_inventory/trader_joes_inventory/")

import scrapy
from scrapy.shell import inspect_response
import json
from scrapy import Request
from items import TraderJoesInventoryItem

class Main1PySpider(scrapy.Spider):
    name = "main_1.py"
    # allowed_domains = ["x"]
    # start_urls = ["http://x/"]

    url = 'https://www.traderjoes.com/api/graphql'

    payload = {
        "operationName": "SearchProducts",
        "variables": {
            "storeCode": "TJ",
            "availability": "1",
            "published": "1",
            "categoryId": 2,
            "currentPage": 1,
            "pageSize": 10
        },
        "query": "query SearchProducts($categoryId: String, $currentPage: Int, $pageSize: Int, $storeCode: String = \"TJ\", $availability: String = \"1\", $published: String = \"1\") {\n  products(\n    filter: {store_code: {eq: $storeCode}, published: {eq: $published}, availability: {match: $availability}, category_id: {eq: $categoryId}}\n    currentPage: $currentPage\n    pageSize: $pageSize\n  ) {\n    items {\n      sku\n      item_title\n      category_hierarchy {\n        id\n        name\n        __typename\n      }\n      primary_image\n      primary_image_meta {\n        url\n        metadata\n        __typename\n      }\n      sales_size\n      sales_uom_description\n      price_range {\n        minimum_price {\n          final_price {\n            currency\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      retail_price\n      fun_tags\n      item_characteristics\n      __typename\n    }\n    total_count\n    pageInfo: page_info {\n      currentPage: current_page\n      totalPages: total_pages\n      __typename\n    }\n    aggregations {\n      attribute_code\n      label\n      count\n      options {\n        label\n        value\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    }

    headers = {
        'authority': 'www.traderjoes.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'AMCVS_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=1; affinity="60ebb3f313f159a3"; AMCV_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=-2121179033%7CMCIDTS%7C19424%7CMCMID%7C73490636295937678721064277091182230025%7CMCOPTOUT-1678277182s%7CNONE%7CvVersion%7C5.3.0',
        'dnt': '1',
        'origin': 'https://www.traderjoes.com',
        'referer': 'https://www.traderjoes.com/home/products/category/products-2',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }


    def start_requests(self):
        self.payload.update({"variables":{
            "storeCode": "TJ",
            "availability": "1",
            "published": "1",
            "categoryId": 2,
            "currentPage": 1,
            "pageSize": 10
        }})
            
        yield scrapy.Request(url=self.url, method='POST', headers=self.headers, body=json.dumps(self.payload), callback=self.paginate)
    
    def paginate(self,response):
        raw_data = json.loads(response.body)
        total_page = raw_data['data']['products']['pageInfo']['totalPages']
        
        for i in range(1,total_page):
            self.payload.update({"variables":{
                "storeCode": "TJ",
                "availability": "1",
                "published": "1",
                "categoryId": 2,
                "currentPage": i,
                "pageSize": 10
            }})
            
            yield scrapy.Request(url=self.url, method='POST', headers=self.headers, body=json.dumps(self.payload), callback=self.parse)
    
    # def parse(self, response):
    #     raw_data = json.loads(response.body)
    #     total_item = len(raw_data['data']['products']['items'])
    #     for j in range(0,total_item):
    #         try:
    #             item ={
    #                 'Item Name' : raw_data['data']['products']['items'][j]['item_title'],
    #                 'Main Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][1]['name'],
    #                 'Sub Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][2]['name'],
    #                 'Sub sub Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][3]['name'],
    #                 'Price, '+ raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value'],
    #                 'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                 'Size Unit' : raw_data['data']['products']['items'][j]['sales_uom_description'],
    #                 # 'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                 'SKU' : raw_data['data']['products']['items'][j]['sku'],
    #             }
    #             yield item
    #         except IndexError:
    #             try:                    
    #                 item ={
    #                     'Item Name' : raw_data['data']['products']['items'][j]['item_title'],
    #                     'Main Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][1]['name'],
    #                     'Sub Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][2]['name'],
    #                     'Price, '+ raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value'],
    #                     'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                     'Size Unit' : raw_data['data']['products']['items'][j]['sales_uom_description'],
    #                     # 'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                     'SKU' : raw_data['data']['products']['items'][j]['sku'],
    #                 }
    #                 yield item
    #             except :                    
    #                 item ={
    #                     'Item Name' : raw_data['data']['products']['items'][j]['item_title'],
    #                     'Main Category' : raw_data['data']['products']['items'][j]['category_hierarchy'][0]['name'],
    #                     'Price, '+ raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value'],
    #                     'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                     'Size Unit' : raw_data['data']['products']['items'][j]['sales_uom_description'],
    #                     # 'Packaging size' : raw_data['data']['products']['items'][j]['sales_size'],
    #                     'SKU' : raw_data['data']['products']['items'][j]['sku'],
    #                 }
    #                 yield item

    def parse(self, response):
        raw_data = json.loads(response.body)
        total_item = len(raw_data['data']['products']['items'])
        inventory = TraderJoesInventoryItem()
        for j in range(0,total_item):
            try:
                inventory['Item_Name'] : raw_data['data']['products']['items'][j]['item_title']
                inventory['Main_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][1]['name']
                inventory['Sub_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][2]['name']
                inventory['Sub_Sub_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][3]['name']
                inventory['Price']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value']
                inventory['Currency'] : raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']
                inventory['Packaging_Size'] : raw_data['data']['products']['items'][j]['sales_size']
                inventory['Size_Unit'] : raw_data['data']['products']['items'][j]['sales_uom_description']
                inventory['SKU'] : raw_data['data']['products']['items'][j]['sku']
                yield inventory
            except IndexError:
                try:                    
                    inventory['Item_Name'] : raw_data['data']['products']['items'][j]['item_title']
                    inventory['Main_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][1]['name']
                    inventory['Sub_Sub_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][3]['name']
                    inventory['Price']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value']
                    inventory['Currency'] : raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']
                    inventory['Packaging_Size'] : raw_data['data']['products']['items'][j]['sales_size']
                    inventory['Size_Unit'] : raw_data['data']['products']['items'][j]['sales_uom_description']
                    inventory['SKU'] : raw_data['data']['products']['items'][j]['sku']
                    yield inventory
                except :                    
                    inventory['Item_Name'] : raw_data['data']['products']['items'][j]['item_title']
                    inventory['Main_Category'] : raw_data['data']['products']['items'][j]['category_hierarchy'][1]['name']
                    inventory['Price']: raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['value']
                    inventory['Currency'] : raw_data['data']['products']['items'][j]['price_range']['minimum_price']['final_price']['currency']
                    inventory['Packaging_Size'] : raw_data['data']['products']['items'][j]['sales_size']
                    inventory['Size_Unit'] : raw_data['data']['products']['items'][j]['sales_uom_description']
                    inventory['SKU'] : raw_data['data']['products']['items'][j]['sku']
                    yield inventory