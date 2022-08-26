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
#+++++++++++++++++++++++++++++++++++++++++++++++==疫情数据处理==++++++++++++++++++++++++++++++++++++++++++++++++++++++
import pandas as pd

# 1. 准备数据
# 1.1 加载数据
datas = pd.read_json('./世界各国疫情数据.json')

# 1.2 按照累计确诊数量, 对数据进行排序, 获取从确诊数量从高到低的国家名称
datas.sort_values(by='confirmedCount', ascending=False, inplace=True)
country_names = datas['countryName'].unique()

# 1.3 使用透视表,统计每一天, 每个国家的确诊人数
final_data = datas.pivot_table('currentConfirmedCount', index='dateId', columns='countryName')
# 调整列的顺序
final_data = final_data[country_names]

# 1.4 使用0填充缺失值
final_data.fillna(0, inplace=True)

# 1.5 把每一天, 每个国家的确诊人数写入文件
final_data.to_csv('./世界各国疫情数据.csv')
