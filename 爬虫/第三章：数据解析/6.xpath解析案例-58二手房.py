# import requests
# from lxml import etree
# url='https://xinzhou.58.com/ershoufang/'
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
# page_text=requests.get(url=url,headers=headers).text
# #parser=etree.HTMLParser(encoding='utf-8')
# tree=etree.HTML(page_text)
# fp=open('./58txt','w',encoding='utf-8')
# title=tree.xpath('//section[@class="list"]//h3/text()')#title=tree.xpath('//section[@class="list"]//h3/@title')
# for ti in title:
#     fp.write(ti+'\n')
import requests
from lxml import etree
url='https://v26-web.douyinvod.com/4a2575770051ceeabbc9b128a6d6ce1a/625134ff/video/tos/cn/tos-cn-ve-15-alinc2/0a42173486a24eec99da266988167bfc/?a=6383&br=1162&bt=1162&cd=0%7C0%7C0%7C0&ch=26&cr=0&cs=0&cv=1&dr=0&ds=3&er=&ft=iDIGbiNN6VQ9wU0cdjlW.CI_i58hbhdxwin7_4kag36&l=021649485525769fdbddc0200fff0030a92e96d000000717545e1&lr=all&mime_type=video_mp4&net=0&pl=0&qs=0&rc=MzN3djg6Zmw7OjMzNGkzM0ApOTs2NDM2Nzw0N2RmNWc1NWdhYTJzcjRnMGNgLS1kLTBzczY0NDYyY15eXi5hNmFfNi46Yw%3D%3D&vl=&vr='
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
page_text=requests.get(url=url,headers=headers).content
#parser=etree.HTMLParser(encoding='utf-8')
fp=open('./.mp4','wb')
fp.write(page_text)
