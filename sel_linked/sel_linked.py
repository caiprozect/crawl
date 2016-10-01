import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.proxy import *

USER = sys.argv[1]
PASS = sys.argv[2]
FILE = "img_urls_test.json"

profile = FirefoxProfile("/Users/caiprozect/Library/Application Support/Firefox/Profiles/mrjqbcaq.sel_profile")
#profile = FirefoxProfile("C:/Users/cai/AppData/Roaming/Mozilla/Firefox/Profiles/g20kvwve.sel_profile")
profile.set_preference("general.useragent.override", "Mozilla/5.0(compatible; Googlebot/2.1; +http://www.google.com/bot.html)")

driver = webdriver.Firefox(firefox_profile = profile)
driver.get("http://www.linkedin.com")

user_field = driver.find_element_by_name("session_key")
pass_field = driver.find_element_by_name("session_password")

user_field.send_keys(USER)
pass_field.send_keys(PASS)
pass_field.send_keys(Keys.ENTER)

try:
	people_opt = WebDriverWait(driver, 60).until(
		EC.presence_of_element_located((By.XPATH, "//option[@class='people']"))
	)
	people_opt.click()
finally:
	print "\n\npeople option selected.\n\n"

try:
	search_box = WebDriverWait(driver, 60).until(
		EC.presence_of_element_located((By.ID, "main-search-box"))
	)
	search_box.send_keys("microsoft")
	search_box.send_keys(Keys.ENTER)
finally:
	print "\n\nsearch is done.\n\n"
	
try:
	while True:
		results = WebDriverWait(driver, 60).until(
			EC.presence_of_element_located((By.ID, "results"))
		)
		results_list = results.find_elements_by_xpath("./li")
		
		for li in results_list:
			if "people" in li.get_attribute("class"):
				img = li.find_element_by_xpath("./a/img")
				with open(FILE, 'a') as outfile:
					outfile.write(img.get_attribute("src") + '\n')
		def check_existence(string):
			try:
				driver.find_element_by_class_name("next")
			except NoSuchElementException:
				return False
			return True 			
		if check_existence("next"):			
			next = driver.find_element_by_class_name("next")
			next_url = next.find_element_by_xpath("./a").get_attribute("href")
			driver.get(next_url)
		else : break
	
finally:
	print "\n\ngot the image\n\n"
