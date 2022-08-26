import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from lxml import etree
plt.rcParams['font.sans-serif'] = ['KaiTi']
url = "https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0"
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}
res = requests.get(url=url,headers=headers)
res.encoding = "utf-8"
content = res.text
html = etree.HTML(content)
con = html.xpath('//*[@id="fetchRecentStatV2"]/text()')
con = str(con)
begin = con.index("[{")
end = con.index("}catch(e){}']")
con = con[begin : end]
ls = json.loads(con)
# ==============================绘图====================================================
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
    plt.figure('基本柱状图',figsize=(8,6),facecolor='y')
    plt.title("近期风险地区疫情本土新增")
    plt.xlabel("省份")
    plt.ylabel("人数")
    plt.yticks(range(0,99))
    for i,j in zip(range(len(y)), y):
        plt.text(i, j, j)#(i,j)表示添加标签的位置，j表示添加的内容
    plt.grid(color='0.5', linestyle='--', linewidth='1', axis='y')
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.09, top=0.9)
    plt.bar(x, y,width=0.8,alpha=0.5,color='g')
    plt.show()
btxzzt()