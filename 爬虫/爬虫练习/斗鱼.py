import json
import os
import csv
import requests
class DySpider():
    def __init__(self):
        self.num = int(input('输入爬取的页数:'))
        # self.url='https://www.douyu.com/wgapi/ordnc/live/web/room/yzList/%d'
        self.url='https://www.douyu.com/gapi/rkc/directory/mixList/2_1/%d'#lol区
        self.headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 SLBrowser/8.0.0.3161 SLBChan/25'
        }
        f = open('./斗鱼.csv', 'w', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(f, fieldnames=[
            "主播昵称",
            '用户id',
            '直播分类',
            '房间名',
            '直播热度',
            '直播间地址',
            '主播图片地址'
        ])
        self.csv_write.writeheader()
        if not os.path.exists('./斗鱼图片'):
            os.mkdir('./斗鱼图片')
    def send_request(self,url):
        res=requests.get(url=url,headers=self.headers).text
        res=json.loads(res)
        datas=res['data']['rl']
        self.parse_html(datas)
    def parse_html(self,datas):
        for data in datas:
            dict={
                "主播昵称":data['nn'],
                '用户id':data['uid'],
                '直播分类':data['c2name'],#直播分类
                '房间名':data['rn'],#房间名
                '直播热度':data['ol'],#直播热度
                '直播间地址':'https://www.douyu.com/%s'%data['rid'],
                '主播图片地址':data['rs_ext'][2]['rs16']
            }
            print(dict)
            self.save(dict)
    def save(self,dict):
        self.csv_write.writerow(dict)
        content = requests.get(url=dict['主播图片地址'], headers=self.headers).content
        with open('./斗鱼图片/'+dict['主播昵称']+'.jpg','wb') as fp:
            fp.write(content)
    def start(self):
        for i in range(1, self.num + 1):
            url = self.url % i
            self.send_request(url)
if __name__ == '__main__':
    dy=DySpider()
    dy.start()






