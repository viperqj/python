#需求
import requests
url='https://www.baidu.com/s?wd=ip'
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
response= requests.get(url=url,headers=headers,proxies={'https':'115.209.183.68:4213'})
response.encoding='utf-8'
page_text=response.text
fp=open('./ip.html','w',encoding='utf-8')
fp.write(page_text)








