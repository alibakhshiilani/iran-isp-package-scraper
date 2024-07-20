import scrapy

class IrancellSpider(scrapy.Spider):
    name = "irancell"

    def start_requests(self):
        yield scrapy.Request(
            url="https://irancell.ir/e/products/5e16bfacd11fd7209ba56b22",
            callback=self.parse,
        )

    def parse(self, response):
        self.logger.info(f"Response status: {response.status}")

        packages = response.json()
        self.logger.info(f"found {len(packages)} packages")

        for package in packages:
            title = package.get("name", {}).get("en", "").strip()
            period = package.get("specification_contents", [{}])[1].get("desc", {}).get("en", "").strip()  # Assuming time is in the second item
            code = package.get("desc", {}).get("en", "").strip()
            price = package.get("price", "")
            yield {
                    'title': title,
                    'volume': title,
                    'price': price,
                    'period': period,
                    'code': code
            }