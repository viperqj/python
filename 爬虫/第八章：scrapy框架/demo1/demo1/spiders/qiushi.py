import scrapy
from demo1.items import Demo1Item

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    # allowed_domains = ['www.qiushidabaike.com']
    start_urls = ['http://www.qiushidabaike.com/']

#     def parse(self, response):
# #        解析作者的名称+段子内容
#         dl_list=response.xpath('//div[@class="main-left fl"]/dl')
#         all_data=[]
#         for dl in dl_list:
#             #xpath返回的是列表,但是列表元素一定是Selector类型的对象
#             #extract()可以将Selector对象中data参数存储的字符串提取出来
#             # author=dl.xpath('./dt/span/a/text()')[0].extract()
#             author = dl.xpath('./dt/span/a/text()').extract_first()#列表中只有一个元素可以使用extract_first()
#             text = dl.xpath('./dd[1]//text() | ./dd[1]/p//text()').extract()
#             text=''.join(text)
#             dic={
#                 'author':author,
#                 'text':text
#             }
#             all_data.append(dic)
#          return all_data
    def parse(self, response):
        #        解析作者的名称+段子内容
        dl_list = response.xpath('//div[@class="main-left fl"]/dl')
        all_data = []
        for dl in dl_list:
            # xpath返回的是列表,但是列表元素一定是Selector类型的对象
            # extract()可以将Selector对象中data参数存储的字符串提取出来
            # author=dl.xpath('./dt/span/a/text()')[0].extract()
            author = dl.xpath('./dt/span/a/text()').extract_first()  # 列表中只有一个元素可以使用extract_first()
            text = dl.xpath('./dd[1]//text() | ./dd[1]/p//text()').extract()
            text = ''.join(text)
            item=Demo1Item()
            item['author']=author
            item['text']=text
            yield item#将item提交给了管道
