# import pymysql
# connect=pymysql.connect( # 主机名
#             host='127.0.0.1',
#             # 用户名
#             user='root',
#             # 密码
#             password='123456',
#             # 数据库
#             database='rxkc',
#             # 数据库编码
#             charset='utf8',)
# print(connect)
import mysql.connector
connect=mysql.connector.connect( # 主机名
            host='127.0.0.1',
            # 用户名
            user='root',
            # 密码
            password='123456',
            # 数据库
            database='rxkc',
            # 数据库编码
            charset='utf8',)
cursor=connect.cursor()
sql='insert into qcomments (用户名,时间,地点,评论,点赞数) values (%s,%s,%s,%s,%s)'
val=('qj','dcm','a','b',1)

cursor.execute(sql,val)
connect.commit()
print(cursor.rowcount,'插入成功')