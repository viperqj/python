import requests
from lxml import etree
#实例化好一个etree对象，且将解析的源码加载到了该对象中
parser=etree.HTMLParser(encoding='utf-8')
tree=etree.parse('test.html',parser=parser)
#r=tree.xpath('/html/head/title')
#r=tree.xpath('/html//title')
#r=tree.xpath('//title')
#r=tree.xpath('//div[@class="sal"]/title[3]')
#r=tree.xpath('//div[@class="wrap-userbar module"]//li[5]/a/text()')[0]
r=tree.xpath('//div[@class="wrap-userbar module"]//li[5]/a/@href')
print(r)