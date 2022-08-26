'''UA：User-Agent(请求载体的身份标识)
UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
则说明该请求是一个正常的请求。但是，如果检测到请求的载体身份标识不属于某一浏览器，则说明该请求不是
正常的请求（爬虫）
UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
'''
import requests
if __name__=="__main__":
    #UA伪装：将对应的user-agent封装到一个字典中
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
    url='https://www.sogou.com/web?'
    #处理url携带的参数：封装到字典中
    kw=input('enter a word')
    param={'query':kw}
    #对指定的url发起请求
    response=requests.get(url=url,params=param,headers=headers)
    response.encoding='utf-8'
    page_text=response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')