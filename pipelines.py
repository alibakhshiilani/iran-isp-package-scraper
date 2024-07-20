from scrapy import signals
import json

class DataPipeline:
    def __init__(self, filename='items.json'):
        self.filename = filename
        self.items = []

    def process_item(self, item):
        self.items.append(item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        filename = crawler.settings.get('DATA_PIPELINE_FILENAME', 'items.json')
        pipeline = cls(filename=filename)
        crawler.signals.connect(pipeline.spider_closed, signal=signals.spider_closed)
        return pipeline

    def spider_closed(self):
        with open(self.filename, 'w') as f:
            json.dump(self.items, f, indent=4)

    def get_items(self):
        return self.items
