'''在Python中，'|'运算符默认在整数类型和集合类型上定义。
如果两个操作数是整数，那么它将执行bitwise or，这是一个数学运算。
如果两个操作数是set类型，'|'运算符将返回两个集的并集。'''
import requests
from lxml import etree
url='http://www.aqistudy.cn/historydata/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
#a_list_city=tree.xpath('//div[@class="bottom"]/ul/li/a/text() |//div[@class="bottom"]/ul/div[2]/li/a/text()')
a_list_city=tree.xpath('//div[@class="bottom"]/ul/li/a |//div[@class="bottom"]/ul/div[2]/li/a')
all_city_name=[]
for a in a_list_city:
    city_name = a.xpath('./text()')[0]
    all_city_name.append(city_name)
all_city_name=set(all_city_name)
fp=open('./city.txt', 'w', encoding='utf-8')
for i in all_city_name:
    fp.write(i+' ')






















