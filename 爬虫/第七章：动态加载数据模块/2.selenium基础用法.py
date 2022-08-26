from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from lxml import etree
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://scxk.nmpa.gov.cn:81/xk/')
#page_source获取浏览器当前页面的页面源码数据
page_text =driver.page_source
#解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
driver.quit()


