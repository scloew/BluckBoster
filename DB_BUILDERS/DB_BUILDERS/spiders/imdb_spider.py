import scrapy
import re


class ImdbSpider(scrapy.Spider):

    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']
    data = []

    def parse(self, response):
        stars_helper = lambda e: re.findall(r'title=\"(.*?)\"', e)[0].replace(r' (dir.)', '').split(r', ')

        titles = response.css('[class="titleColumn"] a::text').getall()
        cast = map(stars_helper, response.css('[class="titleColumn"]').getall())
        years = map(lambda year: re.findall(r'\d{4}', year), response.css('[class="titleColumn"] span::text').getall())
        ratings = response.css('[class="ratingColumn imdbRating"] strong::text').getall()


        #@TODO use for loop to pipe data to DB
        for t, cast, yr, r in zip(titles, cast, years, ratings):
            pass
