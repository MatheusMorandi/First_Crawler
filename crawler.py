
import scrapy

from items import FirstCrawlerItem

class Crawler(scrapy.Spider):

    name = 'crawler'

    start_urls = [
    
        'https://quotes.toscrape.com'

    ]

    def parse(self, response):

        itens = FirstCrawlerItem()

        todas_div_citacoes = response.css('div.quote')
        
        for citacoes in todas_div_citacoes:

            frase = citacoes.css("span.text::text").get()

            autor = citacoes.css(".author::text").get()

            tag = citacoes.css(".tag::text").getall()

            itens['frase'] = frase

            itens['autor'] = autor

            itens['tag'] = tag

            yield itens

        prox_pagin = response.css("li.next a::attr(href)").get()

        if prox_pagin is not None :

            yield response.follow(prox_pagin, callback = self.parse)