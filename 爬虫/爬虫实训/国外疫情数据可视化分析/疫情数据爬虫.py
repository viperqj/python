import json
import requests
from lxml import etree
from tqdm import tqdm
import re
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0"
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}
res = requests.get(url=url,headers=headers)
res.encoding = "utf-8"
content = res.text #获取响应数据.text返回的是字符串形式的响应数据
html = etree.HTML(content)
con = html.xpath('//*[@id="getListByCountryTypeService2true"]/text()')
ls=con[0][48:198305-56]

# ==============================数据解析====================================================
datas = []#存放 国家名+此国家详情链接
detail_datas=[]#国家疫情详情
ex=r'"provinceName":"(?P<provinceName>.*?)".*?"statisticsData":"(?P<statisticsData>.*?)"'
result=re.finditer(ex,ls,re.S)
#把所有的结果放在一个迭代器内
for item in result:
    # provinceName=item.group('provinceName')
    # statisticsData=item.group('statisticsData')
    # print(provinceName,statisticsData)
    datas.append(item.groupdict())
# print(datas[0])
# {'provinceName': '法国', 'statisticsData': 'https://file1.dxycdn.com/2020/0315/929/3402160538577857318-135.json'}
for i in tqdm(datas, '采集世界各国疫情数据'):
    res=requests.get(url=i['statisticsData'],headers=headers).json()
    data=res['data']
    for d in data:
        d['countryName'] =i['provinceName']
        detail_datas.append(d)
        # print(detail_datas)
with open('./世界各国疫情数据.json', 'w', encoding='utf8') as f:
    json.dump(detail_datas, f, ensure_ascii=False)
# json.dumps()是把python对象转换成json对象的⼀个过程，⽣成的是字符串。
# json.dump()是把python对象转换成json对象⽣成⼀个fp的⽂件流，和⽂件相关
# ensure_ascii默认输出ASCLL码，如果把这个该成False就可以输出中⽂