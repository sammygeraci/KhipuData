import scrapy
from scrapy.loader import ItemLoader


class XlsxDownloaderItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()


class KhipuSpider(scrapy.Spider):
    name = "khipu"
    allowed_domains = ["www.khipufieldguide.com"]
    start_urls = ["https://www.khipufieldguide.com/databook/excel_khipus/"]

    def parse(self, response):
        for link in response.xpath("//following::a[6][contains(@href,'xlsx')]"):
            loader = ItemLoader(item=XlsxDownloaderItem(), selector=link)
            relative_url = link.xpath(".//@href").extract_first()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('file_urls', absolute_url)
            yield loader.load_item()
