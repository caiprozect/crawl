#google search "QUERY site:ft.com" then crawl urls...

import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options
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

options = Options()
options.add_argument('--user-agent=Mozilla/5.0(compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
#options.add_argument('user-data-dir=C:/Users/caiprozect/AppData/Local/Google/Chrome/User Data')
#options.add_argument('--load-extension=C:/Users/caiprozect/bypass')
driver = webdriver.Chrome(chrome_options=options)
#raw_input("Press Enter to continue...")
#time.sleep(5)
#driver.get("http://www.ft.com")