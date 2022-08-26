#爬取糗事百科中糗图板块下的所有糗图图片
# content返回的是二进制形式的图片数据 text(字符串) json(对象)
import requests
import os
from bs4 import BeautifulSoup

#创建一个文件夹 用来保存图片
if not os.path.exists('./图片'):
    os.mkdir('./图片')
url='https://www.tupianzj.com/meinv/mm/meituwang//'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
#使用通用爬虫对url对应的一整张页面进行爬取
page_text=requests.get(url=url,headers=headers).text
#使用聚焦爬虫将页面中
soup =BeautifulSoup(page_text,'lxml')
for i in range(0,60):
    img_src_list=soup.select('.tbox  img')[i]['src']
    img_data = requests.get(url=img_src_list).content
    img_name = img_src_list.split('/')[-1]
    # 图片存储路径
    imgPath = './图片/' + img_name
    with open(imgPath, 'wb') as fp:
        fp.write(img_data)
    print('爬取成功666')










