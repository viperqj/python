import pymysql
connect=pymysql.connect(host='localhost',user='root',password='123456',database='rxkc',charset='utf8')
cursor=connect.cursor()
# sql='update qiushi set author="曲江" where text="dcm" '
sql='delete from qiushi where text="xjj"'
cursor.execute(sql)
connect.commit()
print(cursor.rowcount,'修改删除成功')