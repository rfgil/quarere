from scrapy.spiders import SitemapSpider

class GarrafeiraSoaresSpider(SitemapSpider):
    name = 'garrafeira_soares'
    allowed_domains = ['garrafeirasoares.pt']
    sitemap_urls = ['https://www.garrafeirasoares.pt/sitemap_pt.xml']

    def parse(self, response):
      yield {
          'store': self.name,
          'url': response.url,
          'name': response.xpath('//div[contains(@class, "name")]/h1/node()').get(),
          'external_id': response.xpath('//div[@class="ref"]/p/span/node()').get(),
          'price': response.xpath('//div[@class="price"]/h2/span/node()').get().strip(),
          'images': response.xpath('//a[@class="zoom"]/img/@src').getall(),
          'description': response.xpath('//div[contains(@class, "full-desc")]/node()').get().strip(),
          'availability': ''.join(response.xpath('//div[contains(@class, "wrapper-available")]/p[contains(@class, "item-available")]/text()').getall()).strip(),
          'extra_data': dict(zip( # Creates a dict with the first argument as keys and the second as values
              response.xpath('//div[contains(@class, "wrapper-caractrs")]/div/div/p[@class="title"]/node()').getall(),
              response.xpath('//div[contains(@class, "wrapper-caractrs")]/div/div/p[not(@class)]/node()').getall()
          ))
      }
