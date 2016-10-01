from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IMG_FILE = "img_urls_test.json"
FILE = "linked_urls_test_wiht_never_sleep.json"

driver = webdriver.Chrome()

with open(IMG_FILE, 'r') as infile:
	for img_url in infile:
		if "ghost" not in img_url:
			driver.get("http://www.google.com/searchbyimage")

			img_search = WebDriverWait(driver, 60).until(
				EC.presence_of_element_located((By.NAME, "image_url"))
			)

			img_search.send_keys(img_url)
			try:
					linked_url = WebDriverWait(driver, 60).until(
						EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "| LinkedIn"))
					).get_attribute("href")
					with open(FILE, 'a') as outfile:
						outfile.write(linked_url + '\n')
			except: 
					continue