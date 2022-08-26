from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
music=input('输入歌曲名')
num=int(input('输入爬取的评论页数（一页25条评论）:'))
s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
#bro = webdriver.Chrome(service=s,options=option)
bro = webdriver.Chrome(service=s)
bro.get('https://y.qq.com/')
bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
bro.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/span/a').click()
bro.maximize_window()
sleep(2)##########################  特别关键 等浏览器加载iframe
bro.switch_to.frame('login_frame')
bro.switch_to.frame('ptlogin_iframe')
bro.find_element(By.XPATH,'//*[@id="switcher_plogin"]').click()
bro.find_element(By.XPATH,'//*[@id="u"]').send_keys('189334909')
bro.find_element(By.XPATH,'//*[@id="p"]').send_keys('qj109222')
bro.find_element(By.ID,'login_button').click()
bro.switch_to.default_content()
sleep(2)
bro.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div[1]/input').send_keys(music)
bro.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[1]/div[1]/button/i').click()
sleep(2)
bro.find_element(By.XPATH,'//*[@id="app"]/div/div[3]/div/div/div[4]/ul[2]/li[1]/div/div[2]/span/a/div/span').click()
# 基础25条，滚一次加25条，0次25，1次50，2次75...
for i in range(0, num + 1):
    bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    sleep(1)
sleep(1)
html=bro.page_source
tree=etree.HTML(html)
comment_list=tree.xpath('//*[@id="comment_box"]/div[5]/ul/li')
fp=open('./歌词评论.txt','w',encoding='utf-8')
for li in comment_list:
    try:
        qname=li.xpath('./div/h4/a/text()')[0]
    except:
        qname=' '
    a = li.xpath('./div/div[1]/text()')[0]
    b = a.split()
    try:
        qtime=b[0]+b[1]
        qlocality=b[2][2:]
    except:
        qtime = b[0]
        qlocality = b[1][2:]
    try:
        qcomment=li.xpath('./div/p/span/text()')[0]
    except:
        qcomment=' '
    try:
        qprise=li.xpath('./div/div[2]/a[1]/text()')[0]
    except:
        qprise=0
    # print(qname,qtime,qlocality,qcomment,qprise)
    print(qcomment)
    fp.write(qcomment+'\n')

