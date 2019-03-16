import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wikispider'

    def start_requests(self):
        urls = [
            'https://pt.wikipedia.org/wiki/Bilheteria_dos_cinemas_no_Brasil_em_2018'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'filmes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)