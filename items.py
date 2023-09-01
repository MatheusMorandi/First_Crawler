
import scrapy

class FirstCrawlerItem(scrapy.Item):

    frase = scrapy.Field()

    autor = scrapy.Field()

    tag = scrapy.Field()
    