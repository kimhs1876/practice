from selenium import webdriver
from bs4 import  BeautifulSoup
import pandas as pd

class NaverStock(object):

    url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
    driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    class_name = ''
    title_ls = []
    price_ls = []
    dict1 = {}
    dict2 = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.driver_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver.page_source, '?') #?
        all_div = soup.find_all('div',{"class":input('클래스명을 입력하세요')}) # code = 005930
        self.title_ls, self.price_ls = [i.find('a').text for i in all_div] #?
        driver.close()

        for i, j in enumerate(self.title_ls, self.price_ls): #?
            self.dict1[i+1] = self.title_ls[i]
            self.dict2[i+1] = self.price_ls[i]


        self.df = pd.DataFrame.from_dict(self.dict1, self.dict2, orient='index') #?
        path = './data/stock.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')
        print(self.dict1)
        print(self.dict2)

if __name__ == '__main__':
    stock = NaverStock()
    stock.scrap()






