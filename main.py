import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from Comment_Crawling import get_comments, scroll_to_end

URL = 'https://www.youtube.com/watch?v=SwO3vNBoKMU'

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(URL)

scroll_to_end(driver)
get_comments(driver)

driver.close()