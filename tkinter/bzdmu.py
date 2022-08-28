import requests
import re
class BzSpider():
    def __init__(self):
        self.url = 'https://www.ibilibili.com/video/%s?'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'
        }
    def send_request(self,url):
        res=requests.get(url=url,headers=self.headers).text
        self.parse_html(res)
    def parse_html(self, res):
        cid = re.findall('aid=.*?&cid=(.*?)&page=1"',res)[0]
        cid_text=requests.get(url='https://api.bilibili.com/x/v1/dm/list.so?oid='+cid,headers=self.headers).text.encode('iso-8859-1').decode('utf8')
        data=re.findall('<d p=".*?">(.*?)</d>',cid_text)
        for i in data:
            print(i)
            self.save(i)
    def save(self,data):
        with open('弹幕.txt','a',encoding='utf-8') as fp:
            fp.write(data+'\n')
    def start(self,name):
        url = self.url % name
        self.send_request(url)
if __name__ == '__main__':
    bz=BzSpider()
    bz.start()
