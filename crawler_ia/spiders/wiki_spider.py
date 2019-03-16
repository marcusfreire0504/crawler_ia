import scrapy
import pickle

class WikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls = [
        'https://pt.wikipedia.org/wiki/Bilheteria_dos_cinemas_no_Brasil_em_2018',
        'https://pt.wikipedia.org/wiki/Bilheteria_dos_cinemas_no_Brasil_em_2012'
    ]

    def parse(self, response):
        file = response.css('table')[1].getall()
        #print(file)

        output = open('filmes.html', 'wb')
        pickle.dump(file, output)
        output.close()