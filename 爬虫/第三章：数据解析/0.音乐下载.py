import requests
#如何爬取图片
url='http://freetyst.nf.migu.cn/public/product9th/product43/2021/04/0813/2021%E5%B9%B404%E6%9C%8808%E6%97%A511%E7%82%B948%E5%88%86%E7%B4%A7%E6%80%A5%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5%E5%8D%8E%E7%BA%B355%E9%A6%96/%E5%85%A8%E6%9B%B2%E8%AF%95%E5%90%AC/Mp3_64_22_16/6005759Z0RK133448.mp3?channelid=02&msisdn=88507bd6-10d8-4277-955f-22ac84346d5a&Tim=1651068104104&Key=e414f5b35d49d5c6'
#content返回的是二进制形式的图片数据
#text(字符串) json(对象)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
img_data=requests.get(url=url,headers=headers).content
with open('./关键词.mp3','wb') as fp:
    fp.write(img_data)













