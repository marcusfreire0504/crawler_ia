import scrapy
import pickle

url = input('Digite a url')

class WikiSpider(scrapy.Spider):
    name = 'wikispider'
    start_urls = [
        url
    ]

    def parse(self, response):
        file = response.css('table')[1].getall()
        output = open('filmes.html', 'wb')
        pickle.dump(file, output)
        output.close()