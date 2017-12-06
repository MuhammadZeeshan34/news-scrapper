from abc import ABCMeta,abstractmethod
import requests, re
from bs4 import BeautifulSoup
import pdb
from urllib3.exceptions import MaxRetryError
import re
import nltk
import os
from nltk.stem.snowball import SnowballStemmer


class CrawlerSpider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_headlines(self):
        NotImplemented("Function not implemented!")

    @abstractmethod
    def get_news_info(self):
        NotImplemented("Function not implemented!")

    @abstractmethod
    def parse_page(self):
        NotImplemented("Function not implemented")




class ReutersCrawlerSpider(CrawlerSpider):

    def __init__(self, language = "English", start_page = 1, page_size = 10):
        self.domain_url = 'http://www.reuters.com'
        self.language = language
        self.business_news_url = os.path.join(self.domain_url,"news","archive","businessNews")
        self.starts_url = os.path.join(self.business_news_url,"?page=1&pageSize=10&view=page")
        self.headers = {'User-agent' : 'Mozilla/11.0'}
        self.params = {'page' : start_page , 'pageSize' : page_size, 'view' : 'page'}




    def parse_page(self, country_name = None):
        response = requests.get(self.starts_url,params=self.params, headers = self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup)
        h3tags = soup.find_all('a',class_='nav-link-subsec')
        for h3 in h3tags:
            if country_name:
                if re.search(country_name,str(h3['href'])):
                    print(h3)
            else:
                print(h3)
            #text = soup.get_text(separator=' ')
            #text = re.sub("[^a-zA-Z]+", " ", text);
            #print(text)








if __name__== "__main__":
    obj = ReutersCrawlerSpider()
    obj.parse()




