import sys
import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginSpider(scrapy.Spider):
	name = 'login'
	start_urls = ['http://www.linkedin.com']

	def __init__(self):
			self.driver = webdriver.Firefox()

	def parse(self, response):
		self.driver.get(response.url)

		field = self.driver.find_element_by_xpath("/html[@class='os-mac']/body[@id='pagekey-uno-reg-guest-home']/div[@class='global-wrapper ']")
		print "\n\n\n"
		print field
		print "\n\n\n"

		
		user_field = self.driver.find_element_by_xpath("/html[@class='os-mac']/body[@id='pagekey-uno-reg-guest-home']/div[@class='global-wrapper ']/div[@class='header']/div[@class='wrapper']/form[@class='login-form']/input[@id='login-email']")
		pass_field = self.driver.find_element_by_xpath("/html[@class='os-mac']/body[@id='pagekey-uno-reg-guest-home']/div[@class='global-wrapper ']/div[@class='header']/div[@class='wrapper']/form[@class='login-form']/input[@id='login-password']")

		user_field.send_keys('cailinkpro@gmail.com')
		pass_field.send_keys('crawltest123')

		pass_field.send_keys(Keys.ENTER)
		

		self.driver.close()

'''
		return scrapy.FormRequest.from_response(
			response,
			formdata={'session_key': 'cailinkpro@gmail.com', 'session_password': 'crawltest123'},
			callback=self.after_login
			)

	def after_login(self, response):
		if "Sign Out" not in response.body:
			self.log("\n\n\nFiled.")
			return

		print self.driver.find_element_by_xpath("/html[@class='os-mac']")
'''

'''
		from scrapy.shell import inspect_response
		inspect_response(response, self)
'''