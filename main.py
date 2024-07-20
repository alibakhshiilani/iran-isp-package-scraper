from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pipelines import DataPipeline
from IrancellSpider import IrancellSpider
from AsiatechSpider import AsiatechSpider

def get_crawler_settings(filename):
    settings = get_project_settings()
    settings.set('ITEM_PIPELINES', {'pipelines.DataPipeline': 1})
    settings.set('DATA_PIPELINE_FILENAME', filename) 
    return settings

def run_irancell_spider():
    filename="irancell.json"
    process = CrawlerProcess(settings=get_crawler_settings(filename=filename))
    pipeline = DataPipeline()
    process.crawl(IrancellSpider, pipeline=pipeline)
    process.start()

    # items = pipeline.get_items()
    # print("Items retrieved from pipeline:")
    # for item in items:
    #     print(item)

def run_asiatech_spider():
    filename="asiatech.json"
    process = CrawlerProcess(settings=get_crawler_settings(filename=filename))
    pipeline = DataPipeline()
    process.crawl(AsiatechSpider, pipeline=pipeline)
    process.start()

if __name__ == "__main__":
    # run_irancell_spider()
    run_asiatech_spider()
