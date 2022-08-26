import scrapy
from quote.items import QuoteItem

"""
Quotes爬虫
"""
class QuotesSpider(scrapy.Spider):
    #爬虫的名称
    name = 'quotes'
    #爬虫的域名
    allowed_domains = ['quotes.toscrape.com']
    #启动的URL
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for each in response.xpath('//div[@class="quote"]'):
            item = QuoteItem()
            # 名人名言文本
            item['text'] = each.xpath('./span/text()').extract()[0]
            # 作者
            item['author'] = each.xpath('.//small/text()').extract()[0]
            tagList = each.xpath('.//a[@class="tag"]/text()').extract()
            # 标签
            item['tags'] = '/'.join(tagList)
            yield item
        # 下一页的页码
        if len(response.xpath('//li[@class="next"]/a/@href').extract())==0:
            pass
        else:
            next = response.xpath('//li[@class="next"]/a/@href').extract()[0]
            # 下一页的URL
            url = response.urljoin(next)
            # 请求下一页，回调函数为parse
            yield scrapy.Request(url=url, callback=self.parse)
# - scrapy crawl spiderName