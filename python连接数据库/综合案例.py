# https://ty.fang.lianjia.com/loupan/
import requests
from lxml import etree
import  pymysql
class LJSpider():
    def __init__(self):
        self.num=int(input('页数:'))
        self.url='https://ty.fang.lianjia.com/loupan/pg%d/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',}
        self.connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='rxkc', charset='utf8')
        self.cursor = self.connect.cursor()
        l = 'drop table if exists lianjia;'
        self.cursor.execute(l)
        sql = '''create table lianjia
                      (id int(2) primary key auto_increment,
                      title varchar(255),
                      address varchar(255),
                      shape varchar(255),
                      area varchar(255),
                      aprice varchar(255),
                      tprice varchar(255),
                      detail varchar(255)
                      );'''
        self.cursor.execute(sql)

    def send_request(self,url):
        res=requests.get(url=url,headers=self.headers)
        res.encoding='utf-8'
        if res.status_code==200:
            self.parse_html(res)
    def parse_html(self,res):
        lst=[]
        html=res.text
        tree=etree.HTML(html)
        li_list=tree.xpath('/html/body/div[3]/ul[2]/li')
        for li in li_list:
            title=li.xpath('./div/div[1]/a/text()')[0]
            address=li.xpath('./div/div[2]//text()')
            address=address[1]+' '+address[5]+' '+address[-2]
            shape=li.xpath('./div/a/span//text()')
            if shape:
                try:
                    shape=shape[0]+shape[1]+shape[2]
                except :
                    try:
                        shape = shape[0] + shape[1]
                    except:
                        shape = shape[0]
            else:
                shape='此处暂无介绍'
            area=li.xpath('div/div[3]/span/text()')
            if area:
                area=area[0]
            else:
                area='此处暂无介绍'
            price=li.xpath('./div/div[6]//text()')
            aprice=price[2]+price[4]
            try:
                tprice = li.xpath('div/div[6]/div[2]/text()')[0]
            except:
                tprice='此处暂无介绍'
            detail=str(li.xpath('div/div[5]/span/text()'))
            detail=detail[2:-2]
            detail=detail.replace("', '",' ')
            lst.append((title,address,shape,area,aprice,tprice,detail))
        self.save(lst)
    def save(self,lst):
        ql='insert into lianjia (title,address,shape,area,aprice,tprice,detail) values (%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.executemany(ql,lst)
        self.connect.commit()
        print(f'{self.cursor.rowcount}条记录插入成功')
    def start(self):
        for i in range(1,self.num+1):
            url=self.url%i
            self.send_request(url)

if __name__ == '__main__':
    lj=LJSpider()
    lj.start()