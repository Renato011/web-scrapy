import scrapy

class tarefaSpider(scrapy.Spider):
    name = 'ikea'
    start_urls = ['https://www.ikea.com/ie/en/cat/furniture-fu001/']

    def parse(self, response):
        for link in response.css('.vn__nav.vn-6-grid a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_categorias)

    def parse_categorias(self, response):
        produtos =  response.css('.pip-product-compact__bottom-wrapper')
        for produto in produtos:
            yield {
                'categoria': produto.css('.pip-header-section__title--small.notranslate::text').get().strip(),
                'nome': produto.css('.pip-header-section__description-text::text').get().strip(),
                'preco': produto.css('.pip-price__integer::text').get(),
                'link': produto.css('.pip-product-compact__wrapper-link::attr(href)').get()
            }

