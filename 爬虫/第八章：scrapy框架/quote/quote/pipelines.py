# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymysql

class QuotePipeline:
    # 初始化
    def __init__(self):
        #连接到MySQL数据库
        self.connect = pymysql.connect(
            # 主机名
            host='127.0.0.1',
            # 用户名
            user='root',
            # 密码
            password='123456',
            # 数据库
            database='rxkc',
            # 数据库编码
            charset='utf8',
        )
        self.cursor = self.connect.cursor()
    # 处理每一条数据
    def process_item(self, item, spider):
        item = dict(item)
        # 数据表名
        table = 'quotes'
        # 字段的名称
        keys = ','.join(item.keys())
        # 字段的值
        values = ','.join(['%s'] * len(item))
        # 构造SQL语句
        sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
        try:
            # 执行SQL语句
            if self.cursor.execute(sql, tuple(item.values())):
                self.connect.commit()
        except:
            print("Failed!")
            self.connect.rollback()
        return item
    # 关闭爬虫
    def close_spider(self, spider):
        # 关闭cursor
        self.cursor.close()
        # 关闭连接
        self.connect.close()