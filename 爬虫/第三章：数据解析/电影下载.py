import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}
urls=[]
titles=[]
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.get('https://v.qq.com/channel/movie?channel=movie&iarea=100024&itype=100005&listpage=1&sort=10&year=-1')
# for i in range(0,2):
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     sleep(2)
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(1)
bb = browser.page_source
tree = etree.HTML(bb)
li_list=tree.xpath('/html/body/div[5]/div/div[2]/div')
for i in li_list:
    href=i.xpath('./a/@href')
    href='https://jx.parwix.com:4433/player/?url='+href[0]
    title=i.xpath('./a/@title')[0]
    urls.append(href)
    titles.append(title)
n=1
for i in titles:
    print('第',n,'个电影',i)
    n=n+1
a=eval(input('请输入下载的电影的序号:'))
browser.get(urls[a-1])
sleep(3)
# element1 =browser.find_element(By.CSS_SELECTOR,'#WANG')
# browser.switch_to.frame(element1)
element2 =browser.find_element(By.XPATH,'//*[@id="myiframe"]')
browser.switch_to.frame(element2)
text = browser.execute_script('return document.documentElement.outerHTML')
tree = etree.HTML(text)
# browser.switch_to.default_content()
src=tree.xpath('//*[@id="video"]/@src')[0]
print(src)
# content=requests.get(url=src,headers=headers).content
# path='./'+titles[a-1][0]+'.mp4'
# fp=open(path,'wb')
# fp.write(content)
print(titles[a-1][0],'下载完成！！！！！！！！')


