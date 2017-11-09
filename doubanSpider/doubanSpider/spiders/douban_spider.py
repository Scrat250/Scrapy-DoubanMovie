#-*- coding:utf-8 -*-

from scrapy.spiders import Request,Spider
from doubanSpider.items import DoubanMovieItem

class DoubanSpider(Spider):
		name = "douban_movie_top250"
		headers = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
		}
		
		def start_requests(self):
				url = 'https://movie.douban.com/top250'
				yield Request(url, headers=self.headers)
				
    #allowed_domains = ["https://www.douban.com"]
    #start_urls = [ "https://movie.douban.com/top250"]

		def parse(self, response):
				item = DoubanMovieItem()
				movies = response.xpath('//div[@class="info"]')
				#xpath('//ol[@class="grid_view"]/li')
				for movie in movies:  
				#xpath('//div[@class="info"]'):
								
						item['movie_name'] = movie.xpath(".//a/span[1]/text()").extract()[0]
						#xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
						#xpath(".//a/span[1]/text()").extract()[0]
						
						item['actor'] = movie.xpath(".//p[1]/text()").extract()[0]
						#xpath(".//span/div[@class='bd']/p/text()").extract()[0]
						
						item['introduction'] = movie.xpath(".//p/span[1]/text()").extract()[0]
						#xpath(".//title/span[@class='inq']/text()").extract()[0]
						
						yield item