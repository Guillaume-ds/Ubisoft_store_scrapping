import scrapy
from scrapy.crawler import CrawlerProcess


"""
Collecting Data from Ubisoft store
"""



class CreateUbiGames(scrapy.Spider):
	name = "ubi_games"
	Names=[]
	Editions=[]
	Prices = []
	Discounts = []

	def start_requests(self):
		urls = ['https://store.ubi.com/fr/all-games']
		for url in urls :
			yield scrapy.Request(url = url, callback = self.parse_games)

	def parse_games(self,response):
		nbResponses = int(response.xpath('//div[@class="results-hits"]/p//text()').extract()[0])
		details = response.xpath('//div[@class="card-details"]')

		GamesNames = details.xpath('.//h2[@class="prod-title"]//text()').extract()
		for game in GamesNames:
			gameName = game.strip()
			self.Names.append(gameName)

		#self.Names = self.Names.reverse()

		GamesEditions = details.xpath('.//h3/text()').extract()
		for game in GamesEditions:
			gameEditions= game.strip()
			self.Editions.append(gameEditions)

		GamesPrices = details.css('div.card-price div.price-wrapper>span.standard-price::text').extract()
		for game in GamesPrices:
			gamePrices= game.strip()
			self.Prices.append(gamePrices)

		GamesDiscounts = details.css('div.deal-percentage::text').extract()
		for game in GamesDiscounts:
			gamediscount = game.strip()
			self.Discounts.append(gamediscount)
		self.Discounts.insert(-4,'-00%') #one game as no discount, but a str "special edition" instead	
		

process = CrawlerProcess()
process.crawl(CreateUbiGames)
process.start()


