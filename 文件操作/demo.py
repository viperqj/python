import os
path=r'E:\pythonstudy\爬虫\第三章：数据解析'
file_name=os.listdir(path)
for i in file_name:
    if i.endswith('.py'):
        print(i)

