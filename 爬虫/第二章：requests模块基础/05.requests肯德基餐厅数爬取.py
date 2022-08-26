import requests
import json
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
ky=input('输入查询的关键字:')
pageindex=input('输入查询的页数：')
pagesize=input('输入爬取的页数：')
param={
    'cname':'',
    'pid':'' ,
    'keyword': ky,
    'pageIndex':pageindex ,
    'pageSize': pagesize}
response=requests.get(url=url,params=param,headers=headers)
response.encoding='utf-8'
obj=response.text
type=ky+'.json'
fp=open(type,'w',encoding='utf-8')
json.dump(obj=obj,fp=fp,ensure_ascii=False)
print('爬取结束！！！')