import scrapy
import requests
import json
from pprint import pprint
from scrapy.shell import inspect_response
import pandas as pd


class Rev01Spider(scrapy.Spider):
    name = "rev0.1"
    allowed_domains = ["x"]
    start_urls = ["http://x/"]

    def parse(self, response):
        pass

    # scrape graphql API
    # use postman to generate the headers, payload
    # use Postman to test the API

    url = "https://www.traderjoes.com/api/graphql?1"

    payload = json.dumps({
    "operationName": "SearchProducts",
    "variables": {
        "storeCode": "TJ",
        "availability": "1",
        "published": "1",
        "categoryId": 8,
        "currentPage": 1,
        "pageSize": 15
    },
    "query": "query SearchProducts($categoryId: String, $currentPage: Int, $pageSize: Int, $storeCode: String = \"TJ\", $availability: String = \"1\", $published: String = \"1\") {\n  products(\n    filter: {store_code: {eq: $storeCode}, published: {eq: $published}, availability: {match: $availability}, category_id: {eq: $categoryId}}\n    currentPage: $currentPage\n    pageSize: $pageSize\n  ) {\n    items {\n      sku\n      item_title\n      category_hierarchy {\n        id\n        name\n        __typename\n      }\n      primary_image\n      primary_image_meta {\n        url\n        metadata\n        __typename\n      }\n      sales_size\n      sales_uom_description\n      price_range {\n        minimum_price {\n          final_price {\n            currency\n            value\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      retail_price\n      fun_tags\n      item_characteristics\n      __typename\n    }\n    total_count\n    pageInfo: page_info {\n      currentPage: current_page\n      totalPages: total_pages\n      __typename\n    }\n    aggregations {\n      attribute_code\n      label\n      count\n      options {\n        label\n        value\n        count\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
    })
    headers = {
    'authority': 'www.traderjoes.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ms;q=0.8,id;q=0.7',
    'content-type': 'application/json',
    'cookie': 'affinity="b6c9555c516afb1b"; AMCVS_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=1; AMCV_B5B4708F5F4CE8D80A495ED9%40AdobeOrg=-2121179033%7CMCIDTS%7C19423%7CMCMID%7C87451869367686946830222819236844976757%7CMCOPTOUT-1678131319s%7CNONE%7CvVersion%7C5.3.0',
    'dnt': '1',
    'origin': 'https://www.traderjoes.com',
    'referer': 'https://www.traderjoes.com/home/products/category/food-8',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63'
    }

    # response = requests.request("POST", url, headers=headers, data=payload)

    def start_requests(self):
        yield scrapy.Request(url=self.url, method='POST', headers=self.headers, body=self.payload, callback=self.parse)
        # yield scrapy.Request(url=self.url, method='POST', headers=self.headers, body=json.dumps(self.payload), callback=self.parse)
    
    def parse(self, response):
        # inspect_response(response, self)
        raw_data = json.loads(response.body)
        data = raw_data['data']['products']['items'][0]['item_title']
        # print('\n\n')
        pprint(data)
        # df =pd.DataFrame(data)
        # print('\n\n')
        # print(df)        

    # pprint(response.text)
