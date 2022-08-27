# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imgsPileLine(ImagesPipeline):

    #就是可以根据图片地址进行图片数据的请求
    def get_media_requests(self, item, info):

        yield scrapy.Request(item['src'])

    #指定图片存储的路径
    def file_path(self, request, item,response=None, info=None):
        name=item['name']
        print("正在下载！！！")
        return name

    def item_completed(self, results, item, info):
        return item #返回给下一个即将被执行的管道类