import json
from scrapy.spiders import Spider
from scrapy.selector import Selector

#scrapyd
class MySpider(Spider):
    name = 'Estado Líquido'
    download_delay = 2
    allowed_domains = ['estadoliquido.pt']
    start_urls = ['https://estadoliquido.pt/pt/catalogo/listProdutos?ajax=1&allprods=true']

    def parse(self, response):
        for product in response.css('div.item'):
            yield {
                'Loja': self.name,
                'Nome':  product.xpath('.//a/@title').get(),
                'Preço': product.xpath('.//div[@class="final"]/text()').get().replace('€', '').replace('.',',').strip(),
                'URL': 'https://estadoliquido.pt' + product.xpath('.//a/@href').get(),
            }
