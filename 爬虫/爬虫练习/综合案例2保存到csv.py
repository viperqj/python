from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
import csv
class QQSpider():
    def __init__(self):
        self.f = open('./data.csv', 'w', encoding='utf-8', newline='')  # a 是追加保存
        self.csv_write = csv.DictWriter(self.f, fieldnames=[
            '昵称',
            '时间',
            '地点',
            '评论内容',
            '点赞',
        ])
        self.csv_write.writeheader()
    def send_request(self):
        s = Service(r"D:\Google\Chrome\Application\chromedriver.exe")
        bro = webdriver.Chrome(service=s)
        bro.get('https://y.qq.com/')
        bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[2]/span/a').click()
        bro.maximize_window()
        sleep(2)  ##########################  特别关键 等浏览器加载iframe
        bro.switch_to.frame('login_frame')
        bro.switch_to.frame('ptlogin_iframe')
        bro.find_element(By.XPATH, '//*[@id="switcher_plogin"]').click()
        bro.find_element(By.XPATH, '//*[@id="u"]').send_keys('1683086299')
        bro.find_element(By.XPATH, '//*[@id="p"]').send_keys('dxl20030203')
        bro.find_element(By.ID, 'login_button').click()
        bro.switch_to.default_content()
        sleep(2)
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/input').send_keys('听说你')
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/button/i').click()
        sleep(2)
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/ul[2]/li[1]/div/div[2]/span').click()
        # 基础25条，滚一次加25条，0次25，1次50，2次75...
        for i in range(0, 4):
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
        html = bro.page_source
        self.parse_html(html)
    def parse_html(self,html):
        dit={}
        tree = etree.HTML(html)
        comment_list = tree.xpath('//*[@id="comment_box"]/div[5]/ul/li')
        for li in comment_list:
            dit['昵称'] = li.xpath('./div/h4/a/text()')[0]
            a = li.xpath('./div/div[1]/text()')[0]
            b = a.split()
            try:
                dit['时间'] = b[0] + b[1]
                dit['地点'] = b[2][2:]
            except:
                dit['时间'] = b[0]
                dit['地点'] = b[1][2:]
            dit['评论内容'] = li.xpath('./div/p/span/text()')[0]
            try:
                dit['点赞'] = int(li.xpath('./div/div[2]/a[1]/text()')[0])
            except:
                dit['点赞'] = 0
            self.save(dit)

    def save(self,dit):
        self.csv_write.writerow(dit)
    def start(self):
        self.send_request()
if __name__ == '__main__':
    qq=QQSpider()
    qq.start()









