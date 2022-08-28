import requests
import re
class BzSpider():
    def __init__(self):
        self.url = 'https://www.bilibili.com/video/%s?'
        self.name=input('请输入B站视频号：')
        self.num=input('输入爬取的评论页数（一页20条）：')
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
        aid = re.findall('cid=.*?&aid=(.*?)"', res)[0]
        data_text=requests.get(url=f'https://api.bilibili.com/x/v2/reply/main?csrf=46ae42b8fed56a875b2ba3846133a00a&mode=3&next={self.num}&oid={aid}&plat=1&type=1',headers=self.headers).json()
        data_list=[i['content']['message']for i in data_text['data']['replies']]
        for i in data_list:
            print(i)
            self.save(i, title)
    def save(self, data, title):
        with open(title + 'pl.txt', 'a', encoding='utf-8') as fp:
            fp.write(data + '\n')
    def start(self):
        url = self.url % self.name
        self.send_request(url)
if __name__ == '__main__':
    bz=BzSpider()
    bz.start()