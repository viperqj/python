# 查询操作步骤
    # ·获取连接对象
    # ·获取cursor对象
    # ·编写SQL语句
    # ·执行SOL语句
    # ·调用fetchall()方法获取返回结果,结果为列表类型
    # 遍历列表
import pymysql
connect=pymysql.connect(host='127.0.0.1',user='root',password='123456',database='rxkc',charset='utf8')
cursor=connect.cursor()
sql='select * from qiushi'
cursor.execute(sql)
result=cursor.fetchall()
for i in result:
    print(i)