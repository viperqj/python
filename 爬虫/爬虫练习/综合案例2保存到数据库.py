from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from lxml import etree
import pymysql
class QQSpider():
    def __init__(self):
        self.connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='rxkc',charset='utf8')
        self.cursor = self.connect.cursor()
        l = 'drop table if exists qcomments;'
        self.cursor.execute(l)
        sql = '''create table qcomments
                              (id int(2) primary key auto_increment,
                              用户名 varchar(255),
                              时间 varchar(255),
                              地点 varchar(255),
                              评论 varchar(255),
                              点赞数 int(2)
                              );'''
        self.cursor.execute(sql)
    def send_request(self):
        music=input('输入歌曲名')
        num=int(input('输入爬取的评论页数（一页25条评论）:'))
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
        bro.find_element(By.XPATH, '//*[@id="u"]').send_keys('1564695819')
        bro.find_element(By.XPATH, '//*[@id="p"]').send_keys('qj20010222qj')
        bro.find_element(By.ID, 'login_button').click()
        bro.switch_to.default_content()
        sleep(2)
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/input').send_keys(music)
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]/button/i').click()
        sleep(2)
        bro.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div[4]/ul[2]/li[1]/div/div[2]/span').click()
        # 基础25条，滚一次加25条，0次25，1次50，2次75...
        for i in range(0, num+1):
            bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            sleep(1)
        html = bro.page_source
        self.parse_html(html)
    def parse_html(self,html):
        tree = etree.HTML(html)
        comment_list = tree.xpath('//*[@id="comment_box"]/div[5]/ul/li')
        for li in comment_list:
            qname = li.xpath('./div/h4/a/text()')[0]
            a = li.xpath('./div/div[1]/text()')[0]
            b = a.split()
            try:
                qtime = b[0] + b[1]
                qlocality = b[2][2:]
            except:
                qtime = b[0]
                qlocality = b[1][2:]
            try:
                qcomment = li.xpath('./div/p/span/text()')[0]
            except:
                qcomment=''
            try:
                qprise = int(li.xpath('./div/div[2]/a[1]/text()')[0])
            except:
                qprise = 0
            self.save(qname, qtime,qlocality, qcomment, qprise)
    def save(self,qname, qtime,qlocality, qcomment, qprise):
        try:
            ql = 'insert into qcomments (用户名,时间,地点,评论,点赞数) values (%s,%s,%s,%s,%s)'
            val=(qname, qtime,qlocality, qcomment, qprise)
            self.cursor.execute(ql,val)
            self.connect.commit()
        except BaseException as e:
            try:
                ql = 'insert into qcomments (用户名,时间,地点,评论,点赞数) values (%s,%s,%s,%s,%s)'
                qname='显示失败'
                val = (qname, qtime, qlocality, qcomment, qprise)
                self.cursor.execute(ql, val)
                self.connect.commit()
                print(e,'名字含有表情，编码错误，此处不显示名字')
            except BaseException as e:
                print(e,'评论中编码错误，跳过')
        print(f'{self.cursor.rowcount}条记录插入成功')

    def start(self):
        self.send_request()
if __name__ == '__main__':
    qq=QQSpider()
    qq.start()









