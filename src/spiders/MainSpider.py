import json
from scrapy.spiders import Spider
from scrapy.selector import Selector

from Quarere.src import ProductItem, ProductLoader

#scrapyd
class MySpider(Spider):
    name = 'Estado Líquido'
    download_delay = 2
    allowed_domains = ['estadoliquido.pt']
    start_urls = ['https://estadoliquido.pt/pt/catalogo/listProdutos?ajax=1&allprods=true']

    def parse(self, response):
        for product in response.css('div.item'):
            loader = ProductLoader(item=ProductItem(), response=response)
            loader.add_value('store', self.name)
            loader.add_xpath('name', './/a/@title')
            loader.add_xpath('price', './/div[@class="final"]/text()')
            loader.add_xpath('link', './/a/@href')

            yield loader.load_item()

            # yield {
            #     'Loja': self.name,
            #     'Nome':  product.xpath('.//a/@title').get(),
            #     'Preço': product.xpath('.//div[@class="final"]/text()').get().replace('€', '').replace('.',',').strip(),
            #     'URL': 'https://estadoliquido.pt' + product.xpath('.//a/@href').get(),
            # }
