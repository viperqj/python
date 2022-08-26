import json
import requests
from lxml import etree
import  csv
from pyecharts.charts import Map
import pandas as pd
from pyecharts import  options as opts
url='https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}
response=requests.get(url=url,headers=headers)
response.encoding = "utf-8"
content=response.text
# print(content)
tree = etree.HTML(content)
con = tree.xpath("/html/body/script[1]/text()")
con = str(con)
begin = con.index("[{")
end = con.index("}catch(e){}']")
con = con[begin : end]
json_list=json.loads(con) #json.loads()方法可用于解析有效的JSON字符串并将其转换为Python字典  dumps: 是将dict转换为string
# print(type(json_list))
f=open('./yq.csv','w',encoding='utf-8',newline='')#a 是追加保存
csv_write=csv.DictWriter(f, fieldnames=[
    '地区',
    '现存确诊',
    '累计确诊',
    '治愈',
    '死亡',
])
csv_write.writeheader()
for li in json_list:
    dit={
        '地区':li['provinceShortName'],   #省份
        '现存确诊':li['currentConfirmedCount'],    #现存确诊
        '累计确诊':li['confirmedCount'], #累计确诊
        '治愈':li['curedCount'],   #治愈
        '死亡':li['deadCount'], #死亡
    }
    # print(dit)
    csv_write.writerow(dit)
#
f.close()#关闭保存文件


# 绘制地图
df=pd.read_csv('yq.csv',encoding='utf-8')
print(df)

china_map=(
    Map()
    .add('现存确诊', [list(i) for i in zip(df['地区'].values.tolist(),df['现存确诊'].values.tolist())],'china')
    .add('累计确诊', [list(i) for i in zip(df['地区'].values.tolist(),df['累计确诊'].values.tolist())],'china')
    .add('治愈', [list(i) for i in zip(df['地区'].values.tolist(),df['治愈'].values.tolist())],'china')
    .add('死亡', [list(i) for i in zip(df['地区'].values.tolist(),df['死亡'].values.tolist())],'china')
    .set_global_opts(
        title_opts=opts.TitleOpts(title='各地区确诊人数'),
        visualmap_opts=opts.VisualMapOpts(max_=200,is_inverse=True)#颜色条0-200

    )
)
china_map.render('./各地区确诊人数.html')
print('各地区确诊人数地图绘制完成')