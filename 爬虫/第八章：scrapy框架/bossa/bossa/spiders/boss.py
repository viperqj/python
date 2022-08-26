import scrapy
from bossa.items import BossaItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhaopin.com/jobs/sj2040']
    url='https://www.zhaopin.com/jobs/sj2040_p%d'
    page_num=1
    #回调函数接受item
    #解析详情页
    def parse_detail(self,response):
        item=response.meta['item']
        job_desc=response.xpath('//*[@id="root"]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]//text()').extract()
        job_desc=''.join(job_desc)
        item['job_desc']=job_desc

        yield item
    #解析首页
    def parse(self, response):
        li_list=response.xpath('//*[@id="root"]/div[1]/section/div[2]/div/ul/li')
        for li in li_list:
            item = BossaItem()
            title=li.xpath('./div[1]/a[1]/div[1]/h2/text()').extract_first()
            item['title']=title
            href=li.xpath('./div[1]/a[1]/@href').extract_first()
            # print(href)
            #对详情页发送请求获取详情页的页面源码数据
            #手动请求的发送
            #请求传参：meta={} 可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(href,callback=self.parse_detail,meta={'item':item})
        #分页操作
        if self.page_num<3:
            new_url=format(self.url%self.page_num)
            self.page_num+=1
            yield scrapy.Request(new_url,callback=self.parse)