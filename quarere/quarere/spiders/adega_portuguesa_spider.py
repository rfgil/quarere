from scrapy.spiders import SitemapSpider

class AdegaPortuguesaSpider(SitemapSpider):
    name = 'adega_portuguesa'
    allowed_domains = ['adegaportuguesa.com']
    sitemap_urls = ['https://www.adegaportuguesa.com/sitemap.xml']

    def parse(self, response):
        yield {
            'store': self.name,
            'url': response.url,
            'name': response.xpath('//h1[@class="product_name"]/text()').get(),
            'external_id': response.xpath('//input[@name="id"]/@value').get(),
            'price': response.xpath('//span[@itemprop="price"]/text()').get().strip(),
            'images': [f'https:{href}' for href in response.xpath('//div[@id="product_slider"]//img/@src').getall()],
            'description':  response.xpath('//span[@itemprop="description"]/p/text()').get(),
            'availability': response.xpath('//meta[@itemprop="availability"]/@content').get(),
            'extra_data': dict(zip( # Creates a dict with the first argument as keys and the second as values
                response.xpath('//span[@itemprop="description"]//p/strong/text()').getall(),
                response.xpath('//span[@itemprop="description"]//p[strong]/text()').getall()
            ))
        }
