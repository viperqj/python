# 批量插入数据操作步骤
# 获取连接对象
# 获取cursor对象
# 编写SQL语句
# ·使用列表赋值
# ·调用executemany()执行sql语句
# ·提交事务
import mysql.connector
connect=mysql.connector.connect(host='127.0.0.1',user='root',passwd='123456',database='rxkc',charset='utf8')
cursor=connect.cursor()
sql='insert into qiushi (author,text) values (%s,%s)'
vals=[
    ('zs','dsb'),
    ('李四','xjj')
]
cursor.executemany(sql,vals)
connect.commit()
print(cursor.rowcount,'条记录插入成功')