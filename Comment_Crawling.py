import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

def scroll_to_end(driver):
    last_page_height = 0
    now_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    while now_page_height != last_page_height:
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") 
        time.sleep(2)
        now_page_height = driver.execute_script("return document.documentElement.scrollHeight")

def get_comments(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    comments = soup.find_all("yt-formatted-string", {"id": "content-text"})
    for i in range(len(comments)):
        comments[i] = comments[i].string
    comments =  list(filter(None, comments))
    print(comments)
