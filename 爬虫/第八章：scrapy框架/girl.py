import scrapy
from sgirl.items import SgirlItem

class GirlSpider(scrapy.Spider):
    name = 'girl'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kdongman/']
    url = 'https://pic.netbian.com/4kdongman/index_%d.html'
    page_num = 2
    n=int(input('请输入你想要爬取的页数(>=2)：'))
#详情页面解析
    def parse_detail(self,response):
        item=response.meta['item']
        name=response.xpath('//*[@id="main"]/div[2]/div[1]/div[1]/h1/text()').extract_first()
        item['name']=name+'.jpg'
        src=response.xpath('//*[@id="img"]/img/@src').extract_first()
        src='https://pic.netbian.com'+src
        item['src']=src
        yield item
#首页数据解析
    def parse(self,response):
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            item = SgirlItem()
            href = li.xpath('./a/@href').extract_first()
            href='https://pic.netbian.com'+href
            # print(href)
            # item['href'] = href
            # 对详情页发送请求获取详情页的页面源码数据
            # 手动请求的发送
            # 请求传参：meta={} 可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(href, callback=self.parse_detail, meta={'item': item})
        # # 分页操作
        if self.page_num <= self.n:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(new_url, callback=self.parse)