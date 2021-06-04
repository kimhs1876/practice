from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

class NaverMovies(object):
    url = 'naver.com'
    drive_path = 'chrome'
    class_name  = []
    title_lsit = []
    dict = {}
    df = None

    def scrap(self):
        driver = webdriver.Chrome(self.drive_path)
        driver.get(self.url)
        soup = BeautifulSoup(driver, page_source, 'html.parser')
        all_div = soup.find_all('div', {"class" : self.class_name})
        self.title_lsit = [ i.find('a').text for i in all_div]
        driver.close()

        for i,j in enumerate(self.title_list):
            self.dict[i+1] = self.title_lsit[i]

            self.df = pd.DataFrame.from_dict(self.dict, orient= 'index')
            path = '???'
            self.df.to_csv(path,sep='',na_rep='NaN')
            print(self.dict)

if __name__ == '__main__':
    naver = NaverMovies()
    naver.scrap()