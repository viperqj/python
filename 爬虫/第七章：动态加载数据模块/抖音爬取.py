import time
import re
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
import os
try:
    if not os.path.exists('./dy短视频'):
        os.mkdir('./dy短视频')
except:
    pass
word=input('请输入目标对象的抖音号：')
douyin_urls=[]
srcs=[]
jy=0
al=-1
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
#bro = webdriver.Chrome(service=s,options=option)
bro = webdriver.Chrome(service=s)
bro.get('https://www.douyin.com/')
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
time.sleep(3)
try:
    bro.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
except:
    bro.find_element(By.XPATH, '//*[@id="verify-bar-close"]').click()
    bro.find_element(By.XPATH, '//*[@id="login-pannel"]/div[2]').click()
aa=bro.find_element(By.XPATH,'//*[@id="douyin-header"]/div/header/div/div/div[1]/div/div[2]/div/div[1]/form/input[1]')
aa.send_keys(word)
sleep(1)
bro.find_element(By.XPATH,'//*[@id="douyin-header"]/div/header/div/div/div[1]/div/div[2]/div/div[1]/button').click()
sleep(1)
windows = bro.window_handles
bro.switch_to.window(windows[-1])
sleep(1)
bro.find_element(By.XPATH,'//*[@id="dark"]/div[2]/div/div[1]/div/div/span[3]').click()
sleep(10)
bro.find_element(By.XPATH,'//*[@id="dark"]/div[2]/div/div[3]/div[3]/ul/li[1]/div/a/div[1]/div[1]').click()
windows = bro.window_handles
bro.switch_to.window(windows[-1])
sleep(1)
for i in range(0,5):
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(2)
sleep(1)
bb = bro.page_source
tree = etree.HTML(bb)
li_list=tree.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li')
for li in li_list:
    cc=li.xpath('./a/@href')[0]
    cc='https:'+cc
    douyin_urls.append(cc)
print(word+'一共有',end='')
print(len(douyin_urls),end='')
print('个作品')
num=eval(input('请输入爬取视频的个数：'))
for url in douyin_urls:
        al=al+1
        if al==num:
            break
        else:
            bro.get(url)
            sleep(1)
            page=bro.page_source
            ex='<source.*?src="(.*?)" type="">'
            src=re.findall(ex,page,re.S)#列表 一共三个网址
            src=src[0]
            if len(src)==0:
                pass
            else:
                src='https:'+src
                srcs.append(src)
for url in srcs:
       jy=jy+1
       print(url)
       content=requests.get(url).content
       ll=url.split('/')[3]
       Path = './dy短视频/' +ll+ '.mp4'
       with open(Path, 'wb') as fp:
            fp.write(content)
       jy=str(jy)
       print('第'+jy+'个作品下载成功666！')
       jy=int(jy)
bro.quit()