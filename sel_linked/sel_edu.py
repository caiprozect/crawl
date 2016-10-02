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
QUERY = "Microsoft"
#INFILE = 'linked_urls_test_wiht_never_sleep.json'
INFILE = 'test_dir.json'
OUTFILE = 'linked_edu_test_2.json'
COUNT = 0

driver = webdriver.Chrome()
driver.get("http://www.linkedin.com")

user_field = driver.find_element_by_name("session_key")
pass_field = driver.find_element_by_name("session_password")

user_field.send_keys(USER)
pass_field.send_keys(PASS)
pass_field.send_keys(Keys.ENTER)

with open(INFILE, 'r') as urls:
	for url in urls:
		print COUNT
		if 'dir' in url:
			driver.get(url)
			try:
				linked_text_lst = driver.find_elements_by_tag_name("a")
				for linked_text in linked_text_lst:
					content = linked_text.find_element_by_xpath("./..").text
					content_text = content.encode('utf-8')
					if QUERY in content_text:
						print content_text
					else:
						continue
			except:
				continue

		else:
			driver.get(url)
			if "Sign In" in driver.page_source:
				pass_field = driver.find_element_by_name("session_password")
				pass_field.send_keys(PASS)
				pass_field.send_keys(Keys.ENTER)
			try:
				schools_div = WebDriverWait(driver, 15).until(
										EC.presence_of_element_located((By.ID, "background-education"))
									)
				school_info = schools_div.text
				#print type(school_info)
				COUNT += 1
				with open(OUTFILE, 'a') as outfile:
					outfile.write(school_info.encode('utf8'))
					outfile.write("\n\n\n")
			except:
				continue

			