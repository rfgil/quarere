from scrapy.spiders import SitemapSpider
import unicodedata
import json

class GarrafeiraNacionalSpider(SitemapSpider):
    name = 'garrafeira_campo_de_ourique_spider'
    allowed_domains = ['garrafeiracampodeourique.pt/product/']
    sitemap_urls = ['https://www.garrafeiracampodeourique.pt/sitemap.xml']
    sitemap_rules = [('/product/', 'parse')]

    def parse(self, response):
        res = json.loads(response.selector.xpath('//script[contains(text(), "var product = ")]/node()').get()[14:-1])

        yield {
            'store': self.name,
            'url': response.url,
            'name': res["title"],
            'external_id': res["id"],
            'price': response.selector.xpath('//span[contains(@class,"data-product-price")]/node()').get(),
            'images': res["image"]["full"],
            'description':  unicodedata.normalize("NFKD", ' '.join(response.selector.xpath('//h1[contains(@class,"product-title")]/..//div[@class="description"]/p/text()').getall())),
            'availability': res["stock"]["stock_qty"] > 0,
            'extra_data': res
        }

# JSON EXAMPLE FROM: https://www.garrafeiracampodeourique.pt/product/gin-mombasa-colonel-s-reserve-70cl
# {
#   "id": 378277,
#   "title": "Gin Mombasa Colonel`s reserve 70cl",
#   "reference": "",
#   "barcode": "",
#   "price": 43.75,
#   "price_formatted": "43,75 \\u20ac",
#   "price_promo": 40,
#   "price_promo_formatted": "40,00 \\u20ac",
#   "promo_show_percentage": false,
#   "price_promo_percentage": null,
#   "price_on_request": false,
#   "created_at": "2021-08-27T15:28:57+01:00",
#   "status": 1,
#   "status_alias": "active",
#   "position": 0,
#   "shipping": 0,
#   "shipping_alone": false,
#   "featured": true,
#   "new": false,
#   "is_promotion": false,
#   "description": "<p>Mombasa Gin Club Colonel&rsquo;s Reserve &eacute; uma edi&ccedil;&atilde;o especial limitada em homenagem a esta ra&ccedil;a particular de homens que foram capazes de conduzir o Imp&eacute;rio Brit&acirc;nico Vitoriano atrav&eacute;s de seu per&iacute;odo mais glorioso, alcan&ccedil;ando fama e reconhecimento mundial.<\\/p>\n<p>O Mombasa Club Colonel&rsquo;s Reserve Gin &eacute; destilado seguindo o m&eacute;todo tradicional conhecido como destila&ccedil;&atilde;o em lote. O gr&atilde;o &eacute; todo proveniente do Reino Unido, &eacute; predominantemente trigo com um pouco de cevada. Nenhum centeio &eacute; usado. Ap&oacute;s tr&ecirc;s destila&ccedil;&otilde;es, os bot&acirc;nicos s&atilde;o deixados para macerar por 48 horas antes que a destila&ccedil;&atilde;o final seja produzida no Tom Thumb 500 litros Pot Still. Esse per&iacute;odo prolongado permite que o &aacute;lcool extraia muito mais sabores e &oacute;leos dos vegetais e d&aacute; um aspecto muito mais intenso e redondo ao produto final.<\\/p>",
#   "excerpt": "Mombasa Gin Club Colonel\\u2019s Reserve \\u00e9 uma edi\\u00e7\\u00e3o especial limitada em homenagem a",
#   "video_url": "",
#   "file": null,
#   "tax": 0,
#   "taxable": false,
#   "reduced_rate": null,
#   "meta_description": "",
#   "meta_tags": "",
#   "handle": "gin-mombasa-colonel-s-reserve-70cl",
#   "page_title": "Gin Mombasa Colonel`s reserve 70cl",
#   "weight": 1200,
#   "sales": 0,
#   "variants_same_values": true,
#   "updated_at": "2021-09-06T15:49:44+01:00",
#   "description_short": "Mombasa Gin Club Colonel\\u2019s Reserve \\u00e9 uma edi\\u00e7\\u00e3o especial limitada em homenagem a",
#   "promo": true,
#   "url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/product\\/gin-mombasa-colonel-s-reserve-70cl",
#   "add_cart_url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/cart\\/add\\/gin-mombasa-colonel-s-reserve-70cl",
#   "wishlist": {
#     "add_url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/wishlist\\/add\\/gin-mombasa-colonel-s-reserve-70cl",
#     "remove_url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/wishlist\\/remove\\/gin-mombasa-colonel-s-reserve-70cl"
#   },
#   "permalink": "https:\\/\\/www.garrafeiracampodeourique.pt\\/product\\/gin-mombasa-colonel-s-reserve-70cl",
#   "video_embed_url": false,
#   "image": {
#     "thumb": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/thumb\\/b4724c1-154058-20210906_140150.jpg",
#     "square": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/square\\/b4724c1-154058-20210906_140150.jpg",
#     "full": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/b4724c1-154058-20210906_140150.jpg"
#   },
#   "images": [],
#   "price_without_tax": 40,
#   "categories": [
#     {
#       "id": 9735,
#       "parent": 0,
#       "active": true,
#       "title": "Destilados",
#       "description": "",
#       "handle": "destilados",
#       "url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/category\\/destilados",
#       "image": {
#         "thumb": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/thumb\\/e2eb0a9-distillation.png",
#         "square": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/square\\/e2eb0a9-distillation.png",
#         "full": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/e2eb0a9-distillation.png"
#       }
#     },
#     {
#       "id": 31734,
#       "parent": 0,
#       "active": false,
#       "title": "Gin",
#       "description": "",
#       "handle": "gin",
#       "url": "https:\\/\\/www.garrafeiracampodeourique.pt\\/category\\/gin",
#       "image": {
#         "thumb": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/thumb\\/e2eb0a9-distillation.png",
#         "square": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/square\\/e2eb0a9-distillation.png",
#         "full": "https:\\/\\/cdn.lojasonlinectt.pt\\/usercontent\\/garrafeira-campo-de-ourique\\/media\\/images\\/e2eb0a9-distillation.png"
#       }
#     }
#   ],
#   "brand": null,
#   "tags": null,
#   "options": [],
#   "option_groups": [],
#   "stock": {
#     "stock_enabled": true,
#     "stock_qty": 6,
#     "stock_backorder": false,
#     "stock_show": false,
#     "stock_sold_single": false,
#     "stock_notify": null
#   },
#   "rating": null,
#   "custom_fields": null,
#   "tabs": null
# }
