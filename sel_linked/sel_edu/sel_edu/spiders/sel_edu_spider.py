import scrapy

class SelEduSpider(scrapy.Spider):
	name = "sel_edu"

	def start_requests(self):
		urls=[
			'https://www.linkedin.com/in/aroraanuj',
			'https://in.linkedin.com/in/harshthakar002',
			'https://www.linkedin.com/in/easyishard',
			'https://in.linkedin.com/in/gksinha',
			'https://uk.linkedin.com/in/debasreesarbadhikary',
			'https://www.linkedin.com/in/indrapal',
			'https://www.linkedin.com/in/nitithakker',
			'https://www.linkedin.com/in/mohitnagpaldce',
			'https://in.linkedin.com/in/mohammadshabaz',
			'https://in.linkedin.com/in/gksinha',
			'https://www.linkedin.com/in/gautam714',
			'https://in.linkedin.com/in/meghaditya',
			'https://www.linkedin.com/in/sunilknarang',
			'https://in.linkedin.com/in/kumaramlendu',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-2]
		filename = 'quetes-%s.html' % page
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)