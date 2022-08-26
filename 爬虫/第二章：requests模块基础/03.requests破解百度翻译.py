import requests
import json
#step 1指定url
post_url='https://fanyi.baidu.com/sug'
#2 进行UA伪装
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
# 3.post请求参数处理（同get）
word=input('enter a word')
data={"kw": word}#数据字典类型
# 4.发起请求
response=requests.post(url=post_url,data=data,headers=headers)
# 5.获取响应数据：json()方法返回的是一个对象obj（只有确认响应数据类型是json，才可以使用json()）
dic_obj=response.json()#字典类型
# 6step持久化存储
print(dic_obj)
# file=word+'.json'
# fp=open(file,'w',encoding='utf-8')
#
# json.dump(dic_obj,fp=fp,ensure_ascii=False)
# print('爬取结束！！！')