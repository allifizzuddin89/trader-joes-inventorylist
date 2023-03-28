# Brief introduction
- Web scraping via API (graphql) request using Scrapy web scraping framework
- Use Postman to generate payload and headers to mimic the real request. Tips : does not work with curl2scrapy
- Extracting Item Name, Main Category, Sub Category, Sub sub category, Price, Currency, Packaging Size, Size Unit SKU
- Use feed exporter to generate csv file
- Store the scraped date into MySQL database
- Include item loader and pipeline.
- MySQL setup in pipelines.py.
- Item/itemloader setup in items.py
- Feedexporter setup in settings.py

## Run
- The working directory is trader-joes-inventorylist/tree/main/trader_joes_inventory/trader_joes_inventory/spiders
- Activate the installed working environment
- Run the main.py in the working directory.
- Run <scrapy runspider main.py> in the terminal in the working directory
  OR simply run <scrapy crawl main.py> or <scrapy runspider whateverworkspacedirectory/main.py>
- Csv will be generated, already included via feed exporter

### Install environment
- Refer [CONDA Environment Installation](https://docs.anaconda.com/anaconda/install/)
 
### HOW-TO
- Clone the repository
```bash  
  git clone https://github.com/allifizzuddin89/trader-joes-inventorylist.git 
```
- Create working environment (skip if already have any working environment)
```bash
  conda create --name scraping_env -c conda-forge python=3.9.13 scrapy=2.7.1
```
- Activate the working environment
```bash
  conda activate scraping_env
```
- Setup MySql Database, please us your own details; host, user, password, database, table. See link below for setup instruction
[MySQL Setup Instruction](https://dev.mysql.com/doc/mysql-getting-started/en/)
 - Run the spider
 ```bash
    scrapy runspider /trader-joes-inventorylist/tree/main/trader_joes_inventory/trader_joes_inventory/spiders/main.py
 ```

## Troubleshoot / guide
- Error might happened due to the payload already expired or request being rejected by the server or the url/api address simply has been changed by the administrator.
  - Please bear in mind, the web owner might change the web's code dynamically anytime. Therefore this web scraping code might not work.
- Solution: 
  1. Refresh the payload and headers using Postman or any API Tool (if any) OR
  2. Using rotating proxy, google it!
  3. Using the new curl in the Postman or any API Tool of your choice.
  4. Items module not found error might happen, please see main.py for further instruction. [main.py](https://github.com/allifizzuddin89/trader-joes-inventorylist/tree/main/trader_joes_inventory/trader_joes_inventory/spiders/)
  
## DISCLAIMER
- This work only meant for educational, research and proof of work purpose only. 
- I will not responsible for any illegal activities.
- Every action is on your own responsibilities.
- Please respect robots.txt.
- Please don't hog down with relentless request, set the interval in the settings.py, under AUTOTHROTTLE. Scrapy made it easy!
