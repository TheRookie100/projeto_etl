import os
import pandas as pd
from dagster import AssetKey, get_dagster_logger, asset
from crawler_noticia.governo.governo.spiders.noticia import G1Spider
from crawler_noticia.economia.economia.spiders.noticia import NoticiasSpider
from scrapy.crawler import CrawlerProcess


@asset 
def crawler_economia() -> None:
    asset_key = AssetKey("economia")
    logger = get_dagster_logger()

    if os.path.exists("data/economia.json"):
        os.remove("data/economia.json")
    os.makedirs("data", exist_ok=True)

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "data/economia.json",
        #'overwrite': True
    })
    
    process.crawl(NoticiasSpider)
    process.start()

    if os.path.exists("data/economia.json"):
        with open("data/economia.json", "r") as f:
            data = f.read()
            logger.info(f"Data for {asset_key}:\n{data}")


@asset 
def crawler_governo() -> None:
    asset_key = AssetKey("governo")
    logger = get_dagster_logger()

    if os.path.exists("data/governo.json"):
        os.remove("data/governo.json")
    os.makedirs("data", exist_ok=True)

    process = CrawlerProcess(settings={
        "FEED_FORMAT": "json",
        "FEED_URI": "data/governo.json",
        #'overwrite': True
    })
    
    process.crawl(G1Spider)
    process.start()

    if os.path.exists("data/governo.json"):
        with open("data/governo.json", "r") as f:
            data = f.read()
            logger.info(f"Data for {asset_key}:\n{data}")