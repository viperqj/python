import requests
#需求：爬取三国演义小说中所有的章节标题和章节内容：https://www.shicimingju.com/book/sanguoyanyi.html
from bs4 import BeautifulSoup
url='https://www.shicimingju.com/book/sanguoyanyi.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
page_text=requests.get(url=url,headers=headers).text.encode('ISO-8859-1')

#在首页中解析出章节的标题和详情页的url
#1.实例化BeautifulSoup对象,需求将页面源码数据加载到该对象中
soup=BeautifulSoup(page_text,'lxml')
#解析章节标题和详情页的url
li_list=soup.select('.book-mulu>ul>li')
fp=open('./sanguo.txt','w',encoding='utf-8')
for li in li_list:
    title=li.a.text
    detail_url='https://www.shicimingju.com/'+li.a['href']
    #对详情页发起请求，解析出章节内容
    detail_page_text=requests.get(url=detail_url,headers=headers).text.encode('ISO-8859-1')
    #解析出详情页中相关的章节内容
    detail_soup=BeautifulSoup(detail_page_text,'lxml')
    content=detail_soup.find('div',class_='chapter_content').text
    fp.write(title+':'+content+'\n')
    print(title,"爬取成功！！！")






