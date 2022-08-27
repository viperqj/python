import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=']
    #链接提取器：根据指定规则(allows=“正则”)进行指定连接提取,从start_urls中提取
    link=LinkExtractor(allow=r'id=1&page=\d+')
    link_detail=LinkExtractor(allow=r'id=\d+')
    rules = (
        #规则解析器:将链接提取器提取到的链接进行指定规则的解析
        Rule(link, callback='parse_item', follow=True),
        # follow=True：可以将链接提取器 继续作用到 连接提取器提取到的链接 所对应的页面中 即例如：在第2个页面中提取第3个页面链接 ...
        Rule(link_detail,callback='parse_detail')
    )
#以下两个方法不可以实现请求传参！
#解析问题编号和问题标题
    #如何将两个方法解析到的数据存到同一个item中，存到两个item中
    def parse_item(self, response):
        li_list=response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            p_num=li.xpath('./span[1]/text()').extract_first()
            p_title=li.xpath('./span[3]/a/text()').extract_first()
            # print(p_num,p_title)
            item=SunproItem()
            item['p_title']=p_title
            item['p_num']=p_num
            yield item
#解析问题具体内容和编号
    def parse_detail(self,response):
        p_content=response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        p_id=response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        # print(p_id,p_content)
        if not p_id:
            print('已处理空值！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
        else:
            p_id=p_id[3:]
            item=DetailItem()
            item['p_content']=p_content
            item['p_id']=p_id
            yield item