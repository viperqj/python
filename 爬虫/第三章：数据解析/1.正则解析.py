#爬取糗事百科中糗图板块下的所有糗图图片
# https://xiaohua.zol.com.cn/qutu/chuangyi/
import requests
import re
import os
import pprint
#创建一个文件夹 用来保存图片
if not os.path.exists('./美图'):
    os.mkdir('./美图')
url='https://www.tupianzj.com/bizhi/DNmeinv/list_77_%d.html'
page_num=1
headers={
'authority':'m.tupianzj.com',
'cookie':'t=11e8ff135d6e427f4e39cfc24cfa275d; r=9436; Hm_lvt_f5329ae3e00629a7bb8ad78d0efb7273=1654062035,1654410359; Hm_lpvt_f5329ae3e00629a7bb8ad78d0efb7273=1654410743',
'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
}
#使用通用爬虫对url对应的一整张页面进行爬取
def pc(url):
    response=requests.get(url=url,headers=headers)
    response.encoding='gbk'
    page_text=response.text
    ex='<li>.*?<img src="(.*?)" alt.*?</li>'
    img_src_list = re.findall(ex,page_text,re.S)#拿到图片网址
    # obj=re.compile(r'<li>.*?<img src="(?P<url>.*?)".*?</li>',re.S)
    # result=obj.finditer(page_text)
    # for item in result:
    #     url=item.group('url')
    #     print(url)
    for src in img_src_list:
        img_data=requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name=src.split('/')[-1]
        #图片存储路径
        imgPath='./美图/'+img_name
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
        print('爬取成功666！！！！！！！！！！！！！！')

def fy(n):
    global page_num
    while page_num<n:
        print('正在爬取%s页'%page_num)
        # new_url=url%page_num
        new_url = format(url % page_num)
        pc(new_url)
        print('第%s页爬取成功'%page_num)
        page_num = page_num + 1
fy(eval(input('请输入爬取的页数：')))











