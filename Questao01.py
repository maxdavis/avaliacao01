import scrapy
import logging 
class Questao01(scrapy.Spider):
    name = "Questao01"
    
    start_urls = {
        'https://www.uol.com.br/'
    }

    def parse(self, response): 
        
        elementos = response.css('#timeline')

        for elemento in elementos:
            cotacao = elemento.css('.currency_quote ::text').extract_first()
               
            yield {'A cotação do dolar é ' : cotacao }