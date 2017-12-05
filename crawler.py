from abc import ABCMeta, abstractmethod
import scrapy
from scrapy.linkextractors import LinkExtractor


class CrawlerSpider(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_headlines(self):
        NotImplemented("Function not implemented!")

    @abstractmethod
    def get_news_info(self):
        NotImplemented("Function not implemented!")




class ReutersCrawlerSpider(CrawlerSpider):

    def __init__(self):
        self.domain_url = 'www.reuters.com'
        self.starts_url = "http://www.reuters.com/news/archive/businessNews?page=1&pageSize=10&view=page"
        self.rules = LinkExtractor(allow=r'\?page=[0-9]&pageSize=10&view=page', restrict_xpaths=('//div[@class="pageNavigation"]'),
                                                        callback='parse_item', follow=True)

        def parse_item(self, response):
            questions = response.xpath('//div[@class="summary"]/h3')

            for question in questions:
                item = StackItem()
                item['url'] = question.xpath(
                    'a[@class="question-hyperlink"]/@href').extract()[0]
                item['title'] = question.xpath(
                    'a[@class="question-hyperlink"]/text()').extract()[0]
                yield item





