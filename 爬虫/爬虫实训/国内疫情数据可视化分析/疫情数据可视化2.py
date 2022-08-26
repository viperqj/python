# 本土新增柱状图
# 本土新增人数地图
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from lxml import etree
from pyecharts.charts import Map
from pyecharts import  options as opts

plt.rcParams['font.sans-serif'] = ['KaiTi']
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0"
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}
res = requests.get(url=url,headers=headers)
res.encoding = "utf-8"
content = res.text #获取响应数据.text返回的是字符串形式的响应数据
html = etree.HTML(content)
con = html.xpath('//*[@id="fetchRecentStatV2"]/text()')
con = str(con)
begin = con.index("[{")
end = con.index("}catch(e){}']")
con = con[begin : end]
ls = json.loads(con)#json.loads()方法可用于解析有效的JSON字符串并将其转换为Python字典  dumps: 是将dict转换为string
# print(type(ls))#<class 'list'>

# ==============================数据分析====================================================
df_data = pd.DataFrame.from_dict(ls)
print(df_data)
def btxzzt():
    ls_provinceShortName = []  # 省份
    ls_yesterdayLocalConfirmedCount= []  # 本土新增确诊
    for x in ls:
        provinceShortName = x["provinceShortName"]
        yesterdayLocalConfirmedCount = x["yesterdayLocalConfirmedCount"]
        ls_provinceShortName.append(provinceShortName)
        ls_yesterdayLocalConfirmedCount.append(yesterdayLocalConfirmedCount)

    x = np.array(ls_provinceShortName)
    y = np.array(ls_yesterdayLocalConfirmedCount)
    plt.title("近期风险地区疫情本土新增")
    plt.xlabel("省份")
    plt.ylabel("人数")
    for i,j in zip(range(len(y)), y):
        # print(i,j,j)
        plt.text(i, j, j)#(i,j)表示添加标签的位置，j表示添加的内容
    plt.bar(x, y)
    plt.show()


# 本土新增人数地图
def dmap():
    ls_provinceShortName=['台湾', '香港', '澳门', '安徽', '广东', '上海', '福建', '天津', '山东', '内蒙古', '北京', '江苏', '重庆', '陕西', '四川', '云南', '浙江', '江西', '海南', '湖北', '湖南', '吉林', '黑龙江', '河北', '辽宁', '甘肃', '河南', '广西', '新疆', '山西', '贵州', '青海', '宁夏', '西藏']
    dict_ls_provinceShortName={}
    for i in ls_provinceShortName:
        dict_ls_provinceShortName[i] = 0
    # {'台湾': 0, '香港': 0, '澳门': 0, '安徽': 0, '广东': 0, '上海': 0, '福建': 0, '天津': 0, '山东': 0, '内蒙古': 0, '北京': 0, '江苏': 0,
    #  '重庆': 0, '陕西': 0, '四川': 0, '云南': 0, '浙江': 0, '江西': 0, '海南': 0, '湖北': 0, '湖南': 0, '吉林': 0, '黑龙江': 0, '河北': 0,
    #  '辽宁': 0, '甘肃': 0, '河南': 0, '广西': 0, '新疆': 0, '山西': 0, '贵州': 0, '青海': 0, '宁夏': 0, '西藏': 0}
    for i in ls:
        provinceShortName=i['provinceShortName']
        yesterdayLocalConfirmedCount=i['yesterdayLocalConfirmedCount']
        dict_ls_provinceShortName[provinceShortName]=yesterdayLocalConfirmedCount

    a=list(dict_ls_provinceShortName.items())

    china_map=(
        Map()
        .add('本土新增',a,'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='近期风险地区疫情本土新增'),
            visualmap_opts=opts.VisualMapOpts(max_=15,is_inverse=True)#颜色条0-20

        )
    )
    china_map.render('./近期风险地区疫情本土新增.html')
    print('本土新增人数地图绘制完成')
btxzzt()
dmap()