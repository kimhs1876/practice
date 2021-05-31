from selenium import webdriver
from bs4 import  BeautifulSoup
import pandas as pd

class NaverStock(object):

    url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ''
    title_ls = []
    price_ls = []
    dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, '?') #?



