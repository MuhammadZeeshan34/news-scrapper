from abc import ABCMeta,abstractmethod
import requests, re
from bs4 import BeautifulSoup
import re
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

    def __init__(self, language = "english", start_page = 1, page_size = 10):
        self.domain_url = 'http://www.reuters.com'
        self.language = language
        self.business_news_url = os.path.join(self.domain_url,"news","archive","businessNews")
        self.starts_url = os.path.join(self.business_news_url,"?page=1&pageSize=10&view=page")
        self.headers = {'User-agent' : 'Mozilla/11.0'}
        self.params = {'page' : start_page , 'pageSize' : page_size, 'view' : 'page'}
        self.stemmer = SnowballStemmer(self.language)




    def parse_page(self, country_name = None, file_path = "/Users/zeeshannawaz/reuters_data.txt"):
        response = requests.get(self.starts_url,params=self.params, headers = self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
       # print(soup)
        tags = soup.find_all('div',class_='story-content')
        #print(tags)
        for tag in tags:
            if country_name:
                if re.search(country_name,str(tag['href'])):
                    print(tag)
            else:
                #print(tag.a['href'])
                article_url = self.domain_url + tag.a['href']
                #print(article_url)
                for sub_response in requests.get(article_url):
                    #print(sub_response)
                    soup = BeautifulSoup(sub_response,'html.parser')
                    text = soup.get_text(separator=' ')
                    text = re.sub("[^a-zA-Z]+", " ", text)
                    words = text.lower().split()
                   # stopwords = nltk.corpus.stopwords.words('english')
                   # words = [w for w in words if not w in stopwords]
                    words = [w for w in words if len(w) > 1]
                    words = [ self.stemmer.stem(w) for w in words ]
                    text = ' '.join(words for words in words if words)
                    with open(file_path,'a') as file:
                        file.write(text)


if __name__== "__main__":
    obj = ReutersCrawlerSpider()
    obj.parse_page()




