import scrapy
from scrapy.utils.response import open_in_browser

class Questao02(scrapy.Spider):
    name = "Questao02"

    canal = 'bicicleta'

    start_urls = {
        'https://lista.mercadolivre.com.br/{}#D[A:{}]'.format(canal,canal)
    }

    def parse(self, response):

        #open_in_browser(response)
        
        divs = response.css('.results')
        conteudo = divs.css('.results-item')
        item =  conteudo.css('.rowItem')
        item_info = item.css('.item__info-container')

        for div in item_info:
            
            nome =  div.css('span.main-title::text').extract_first()
            valor =  div.css('span.price__fraction::text').extract_first()
           
            yield {
                "Nome": nome,
                "Valor": valor               
            }

        NEXT_PAGE_SELECTOR = 'li.andes-pagination__button--next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )