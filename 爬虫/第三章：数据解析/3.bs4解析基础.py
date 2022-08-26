from bs4 import BeautifulSoup
#将本地的html文档加载到该对象中
fp=open('./test.html','r',encoding='utf-8')
soup=BeautifulSoup(fp,'lxml')
#print(soup)
#print(soup.a)
#find('tagname'):===soup.tagname
#print(soup.find('a'))
#
#print(soup.select('.dict-logo'))
#print(soup.select('.dict-logo>a')[0])
#print(soup.select('.dict-logo a'))
#print(soup.select('font')[0].text)








