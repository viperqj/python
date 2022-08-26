import scrapy
from imgsPro.items import ImgsproItem

class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list=response.xpath('//*[@id="container"]/div')
        for div in div_list:
            #注意图片伪属性
            src=div.xpath('./div/a/img/@src2').extract_first()
            src='https:'+src[0:-6]+'.jpg'
            item=ImgsproItem()
            item['src']=src
            yield  item
            # print(src)
