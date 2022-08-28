import requests
import re
class BzSpider():
    def __init__(self):
        self.url = 'https://www.bilibili.com/video/%s?'
        self.name=input('请输入B站视频号：')
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'
        }
    def send_request(self,url):
        res=requests.get(url=url,headers=self.headers).text
        self.parse_html(res)
    def parse_html(self, res):
        title = re.findall('<h1 title="(.*?)"', res)[0]
        # re.sub()替换
        title = re.sub(r'[\/:?*|,.<>"]', '', title)
        cid = re.findall('cid=(.*?)&aid=', res)[0]
        cid_text=requests.get(url='https://api.bilibili.com/x/v1/dm/list.so?oid='+cid,headers=self.headers).text.encode('iso-8859-1').decode('utf8')
        data=re.findall('<d p=".*?">(.*?)</d>',cid_text)
        for i in data:
            print(i)
            self.save(i,title)
    def save(self,data,title):
        with open(title+'dm.txt','a',encoding='utf-8') as fp:
            fp.write(data+'\n')
    def start(self):
        url = self.url % self.name
        self.send_request(url)
if __name__ == '__main__':
    bz=BzSpider()
    bz.start()
