import json
from scrapy.spiders import Spider
from scrapy.selector import Selector

#scrapyd
class MySpider(Spider):
    name = 'Garafeira Nacional'
    download_delay = 2
    allowed_domains = ['garrafeiranacional.com']
    start_urls = [
        'https://www.garrafeiranacional.com/vinho.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/vinho-do-porto.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/whisky.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/generosos.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/destilados.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/premiados.html?p=1&ajax=1',
        'https://www.garrafeiranacional.com/bar.html?p=1&ajax=1'
        ]

    # sitemap_urls = ['https://www.garrafeiranacional.com/sitemap.xml']
    def parse(self, response):
        jsonResponse = json.loads(response.body)

        yield response.follow(jsonResponse["next_page_url"] + "&ajax=1", self.parse)

        html = Selector(text=jsonResponse["html"]["content"])
        for product in html.css('div.product_info'):
            yield {
                'Loja': self.name,
                'Nome':  product.xpath('.//a[@class="product-item-link"]/@title').get(),
                'Preço': product.xpath('.//span[@class="price"]/text()').get().replace('€', '').strip(),
                'URL': product.xpath('.//a[@class="product-item-link"]/@href').get(),
            }

        #yield next_page
