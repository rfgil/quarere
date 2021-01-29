import json
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector

#scrapyd
class MySpider(CrawlSpider):
    name = 'On Wine'
    #download_delay = 2
    allowed_domains = ['onwine.pt']
    start_urls = ['https://www.onwine.pt/vinhos',
    'https://www.onwine.pt/aguardente',
    'https://www.onwine.pt/azeite']

    def parse_start_url(self, response):
        for menu_url in response.xpath('//li[@class="filter"]/a/@href').getall():
            yield response.follow(menu_url, self.parse)

    def parse(self, response):

        next_page = response.xpath('//i[contains(text(),"Next")]/../@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)



        for product in response.css('div.dados-vinho'):

            yield {
                'Loja': self.name,
                'Nome':  product.xpath('./a/h3[@class="vinho-titulo"]/text()').get(),
                'Preço': product.xpath('.//span[@class="new-preco"]/text()').get().replace('€', '').replace('.',',').strip(),
                'URL': 'https://www.onwine.pt' + product.xpath('./a/@href').get(),
            }
