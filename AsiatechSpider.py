import scrapy

class AsiatechSpider(scrapy.Spider):
    name = "asiatech"

    def start_requests(self):
        yield scrapy.Request(
            url="https://www.asiatech.com/page/td-lte/",
            callback=self.parse,
        )

    def parse(self, response):
        self.logger.info(f"Response status: {response.status}")

        tables = response.css(".bd-example > table")
        self.logger.info(f"found {len(packages)} packages")

        for table in tables:
            packages = table.css("tbody > tr")
            for package in packages:
                columns = package.css("td")
                title = columns[0].get().strip()
                price = columns[3].get().strip()
                volume = columns[2].get().strip()
                period = columns[1].get().strip()
                code = columns[4].get().strip()
                if title and volume and period and code:
                    yield {
                            'title': title,
                            'volume': title,
                            'price': price,
                            'period': period,
                            'code': code
                    }
