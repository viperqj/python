import requests
from lxml import etree
import os
if not os.path.exists('.4k/美图'):
    os.mkdir('./4k美图')
num=eval(input('输入想爬取的页数：'))
for i in range(1,num+1):
    i=str(i)
    if i!='1':
        url='https://pic.netbian.com/4kmeinv/index_'+i+'.html'
    else:
        url='https://pic.netbian.com/4kmeinv/'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
    page_text=requests.get(url=url,headers=headers).text.encode('ISO-8859-1')
    tree=etree.HTML(page_text)
    src=tree.xpath('//ul[@class="clearfix"]//img/@src')
    name=tree.xpath('//ul[@class="clearfix"]//b/text()')
    for s,pic_name in zip(src,name):
        href='https://pic.netbian.com'+s
        pic=requests.get(url=href,headers=headers).content
        imgPath = './4k美图/' + pic_name + '.jpg'
        with open(imgPath, 'wb') as fp:
            fp.write(pic)
    print('第'+i+'张网页的图片爬取成功')
print('100%')




# 共通用处理史文乱码的解决方案
# img_name = img_name.encode( 'iso-8859-1 ').decode( ' gbk ')
# Img_name=img_name.encode(‘iso-8859-1’).解码(‘GBK’)



