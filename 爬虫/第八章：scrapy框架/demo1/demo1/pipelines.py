# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class Demo1Pipeline:
    fp=None
    #重写父类的一个方法：该方法只会在开始爬虫的时候被调用一次
    def open_spider(self,spider):
        print('爬虫开始！')
        self.fp = open('./qiushi.txt','w',encoding='utf-8')
    #该方法用来接受爬虫文件提交过来的item对象
    def process_item(self, item, spider):
        author=item['author']
        text=item['text']
        self.fp.write(author+':'+text+'\n')
        return item #传递给下一个即将被执行的管道类

    def close_spider(self,spider):
        print('爬虫结束！')
        self.fp.close()
#管道文件中一个管道类对应将一组数据存储到一个平台或载体中
#将item中的对象存入数据库
class mysqlPileLine:
    conn=None
    cursor = None
    def open_spider(self,spider):
        self.coon = pymysql.Connect(host='127.0.0.1',user='root',password='123456',db='rxkc',charset='utf8')
    def process_item(self, item, spider):
        self.cursor=self.coon.cursor()
        try:
            self.cursor.execute('insert into qiushi values("%s","%s")'%(item["author"],item["text"]))
            self.coon.commit()
        except Exception as e:
            print(e)
            self.coon.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.coon.close()



