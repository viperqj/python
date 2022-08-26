import requests
from bs4 import BeautifulSoup
url='https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CDFD&dbname=CDFDLAST2022&filename=1021095326.nh&uniplatform=NZKPT&v=PBt2wLpCOjPjwf1xxm2nGwcPzD76vbgfMfJCRgrsSztqGYzBOAi9UgYYmJhXQfVv'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
page_text=requests.get(url=url,headers=headers).text
soup=BeautifulSoup(page_text,'lxml')
#content=soup.find('span',id='ChDivSummary').text
content=soup.select('#ChDivSummary')[0].string
with open('./知网论文.txt','w',encoding='utf-8') as fp:
    fp.write(content)
