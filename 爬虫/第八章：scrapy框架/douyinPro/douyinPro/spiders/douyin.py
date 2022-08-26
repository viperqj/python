import scrapy
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from douyinPro.items import DouyinproItem
class DouyinSpider(scrapy.Spider):
    name = 'douyin'
    word=input('请输入目标用户抖音号（芒果捞头条 虹之间-艾克）：')
    # allowed_domains = ['www.douyin.com']
    start_urls = ['https://www.douyin.com/?enter=guide']
    douyin_urls=[]
    option = ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
    # bro = webdriver.Chrome(service=s,options=option)
    bro = webdriver.Chrome(service=s)
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })

    def parse_detail(self, response):
        page_text=response.text
        ex = '<source.*?src="(.*?)" type="">'
        src = re.findall(ex, page_text, re.S)  # 列表 一共三个网址
        if len(src)==0:
            pass
        else:
            src = src[0]
            src = 'https:' + src
            ll = src.split('/')[3]
            name=ll + '.mp4'
            item = DouyinproItem()
            item['src'] = src
            item['name']=name
            yield item
    def parse(self, response):
        li_list=response.xpath('//*[@id="root"]/div/div[2]/div/div/div[4]/div[1]/div[2]/ul/li')
        for li in li_list:
             cc = li.xpath('./a/@href').extract_first()
             cc = 'https:' + cc
             self.douyin_urls.append(cc)
        for href in self.douyin_urls:
            yield scrapy.Request(href, callback=self.parse_detail)


