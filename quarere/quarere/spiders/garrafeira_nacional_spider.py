from scrapy.spiders import SitemapSpider

class GarrafeiraNacionalSpider(SitemapSpider):
    name = 'garrafeira_nacional'
    allowed_domains = ['garrafeiranacional.com']
    sitemap_urls = ['https://www.garrafeiranacional.com/sitemap.xml']

    def parse(self, response):
        yield {
            'store': self.name,
            'url': response.url,
            'name': response.selector.xpath('//span[@itemprop="name"]/node()').get(),
            'external_id': response.selector.xpath('//div[contains(@class, "prod_id")]/node()').get().strip()[4:],
            'price': response.selector.xpath('//span[@class="price"]/node()').get(),
            'images': response.selector.xpath('//div[@class="gallery_main_thumbs"]/img/@src').getall(),
            'description':  response.xpath('//div[@class="product-description-height"]/node()').get().strip(),
            'availability': response.xpath('//div[contains(@class, "stock")]/span/text()').get(),
            'extra_data': dict(zip( # Creates a dict with the first argument as keys and the second as values
                response.selector.xpath('//div[@class="char_name"]//h6/node()').re("\S.*\S"),
                response.selector.xpath('//div[@class="char_name"]/p/a/node()').re("\S.*\S")
            ))
        }
