import requests
import os
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy
# class douyinProPileLine(FilesPipeline):
#
#     def get_media_requests(self, item, info):
#         # 依次对视频地址发送请求，meta用于传递视频的文件名
#         yield scrapy.Request(url=item['src'], meta={'name': item['name']})
#
#     #指定图片存储的路径
#     def file_path(self, request, response=None, info=None, *, item=None):
#         filename = request.meta['name']  # 获取视频文件名
#         return filename  # 返回下载的视频文件名
#
#     #传递给下一个管道类
#     def item_completed(self, results, item, info):
#         return item

class Demo1Pipeline:
    #重写父类的一个方法：该方法只会在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('爬虫开始！')
        try:
            if not os.path.exists('./dy短视频'):
                os.mkdir('./dy短视频')
        except:
            pass
    #该方法用来接受爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        src=item['src']
        name='./dy短视频/'+item['name']
        content = requests.get(url=src, headers=headers).content#二进制数据
        with open(name, 'wb') as fp:
            fp.write(content)
        return item #传递给下一个即将被执行的管道类
    def close_spider(self,spider):
        print('爬虫结束！')