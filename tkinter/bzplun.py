import requests
import re
class BzSpider():
    def __init__(self):
        self.url = 'https://www.ibilibili.com/video/%s?'
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'
        }
    def send_request(self,url,num):
        res=requests.get(url=url,headers=self.headers).text
        self.parse_html(res,num)
    def parse_html(self, res,num):
        aid = re.findall('aid=(.*?)&cid=.*?&page=1"', res)[0]
        data_text=requests.get(url=f'https://api.bilibili.com/x/v2/reply/main?csrf=46ae42b8fed56a875b2ba3846133a00a&mode=3&next={num}&oid={aid}&plat=1&type=1',headers=self.headers).json()
        data_list=[i['content']['message']for i in data_text['data']['replies']]
        for i in data_list:
            print(i)
            self.save(i)
    def save(self, data):
        with open('评论.txt', 'a', encoding='utf-8') as fp:
            fp.write(data + '\n')
    def start(self,name,num):
        url = self.url % name
        self.send_request(url,num)
if __name__ == '__main__':
    bz=BzSpider()
    bz.start()