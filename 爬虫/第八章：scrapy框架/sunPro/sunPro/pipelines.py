# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class SunproPipeline:
    def process_item(self, item, spider):
        #如何判断是那个item
        if item.__class__.__name__== 'SunproItem':
            print(item['p_num'],item['p_title'])
        else:
            print(item['p_id'],item['p_content'])

        return item
class mysqlPileLine:
    conn=None
    cursor = None
    def open_spider(self,spider):
        self.coon = pymysql.Connect(host='127.0.0.1',user='root',password='123456',db='rxkc',charset='utf8')
    def process_item(self, item, spider):
        self.cursor=self.coon.cursor()
        try:
            if item.__class__.__name__ == 'SunproItem':
                self.cursor.execute('insert into sun values("%s","%s")'%(item["p_num"],item["p_title"]))
                self.coon.commit()
            else:
                self.cursor.execute('insert into sunn values("%s","%s")' % (item["p_id"], item["p_content"]))
                self.coon.commit()
        except Exception as e:
            print(e)
            self.coon.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.coon.close()