import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.proxy import *

#USER = sys.argv[1]
#PASS = sys.argv[2]
QUERY = "Microsoft"
INFILE = 'linked_urls_test_wiht_never_sleep.json'
#INFILE = 'test_dir.json'
#INFILE = 'linked_one_dir.json'
OUTFILE = 'linked_bypass_test.json'
#OUTFILE = 'linked_edu_dir_test.json'
#OUTFILE = 'linked_one_dir_test.json'
URLFILE = 'linked_snd_urls_bypass.json'
ERRFILE = 'linked_err_urls_bypass.json'
CNT = 0

options = webdriver.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0(compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://www.linkedin.com")
#test = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "dargrus")))
'''
user_field = driver.find_element_by_name("session_key")
pass_field = driver.find_element_by_name("session_password")

user_field.send_keys(USER)
pass_field.send_keys(PASS)
pass_field.send_keys(Keys.ENTER)
'''

with open(INFILE, 'r') as urls:
	for url in urls:
		time.sleep(10) #check minimal time delay
		if 'dir' in url:
			driver.get(url)
			try:
				body_class = WebDriverWait(driver, 15).until(
						EC.presence_of_element_located((By.TAG_NAME, "body"))
					).get_attribute("class")
			except:
				continue
			if "js guest" in body_class.encode('utf8'):
				result = driver.find_element_by_xpath("//ul[@class='content']")
				linked_text_lst = result.find_elements_by_tag_name("a")
				for linked_text in linked_text_lst:
					content = linked_text.find_element_by_xpath("./..").text
					content_text = content.encode('utf8')
					if QUERY in content_text:
						link = linked_text.get_attribute("href")
						print "writing link..."
						with open(URLFILE, 'a') as urlfile:
							urlfile.write(link)
							urlfile.write('\n')
			else:
				results = driver.find_element_by_id("results")
				li_lst = results.find_elements_by_xpath("./li")
				for li in li_lst:
					desc_text = li.find_element_by_class_name("description").text.encode('utf8')
					if QUERY in desc_text:
						link = li.find_element_by_tag_name("a").get_attribute("href")
						print "writing link..."
						with open(URLFILE, 'a') as urlfile:
							urlfile.write(link)
							urlfile.write('\n')
		elif '/in/' in url:
			try:
				driver.get(url)
			except TimeoutException:
				driver.refresh()
			if "Sign In" in driver.page_source:
				pass_field = driver.find_element_by_name("session_password")
				pass_field.send_keys(PASS)
				pass_field.send_keys(Keys.ENTER)
			try:
				print "trying to find education div..."
				schools_div = WebDriverWait(driver, 15).until(
										EC.presence_of_element_located((By.ID, "education"))
									)
				school_info = schools_div.text
				#print type(school_info)
				with open(OUTFILE, 'a') as outfile:
					CNT += 1
					print CNT
					print "writing education div..."
					outfile.write(school_info.encode('utf8'))
					outfile.write("\n\n\n")
			except:
				print "No education field in this url: " + url
				continue
		else:
			print "Cannot process this url: " + url
			with open(ERRFILE, 'a') as errfile:
				errfile.write(url)
driver.close()