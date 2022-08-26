'''查看当前确诊柱状图 查看疑似病例柱状图
查看当前确诊饼图 查看疑似病例饼图 查看中风险地区柱状图'''
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
content = res.text #获取响应数据.text返回的是字符串形式的响应数据
html = etree.HTML(content)
con = html.xpath("/html/body/script[1]/text()")
con = str(con)
begin = con.index("[{")
end = con.index("}catch(e){}']")
con = con[begin : end]
ls = json.loads(con)#json.loads()方法可用于解析有效的JSON字符串并将其转换为Python字典  dumps: 是将dict转换为string


# ==============================数据分析====================================================
df_data = pd.DataFrame.from_dict(ls)
# print(df_data)



# ==============================数据可视化====================================================
# 绘制柱状图
def qzzzt():
    ls_province = []  # 省份
    ls_currentConfirmedCount = []  # 当前确诊
    for x in ls:
        provinceName = x["provinceShortName"]
        currentConfirmedCount = x["currentConfirmedCount"]
        ls_province.append(provinceName)
        ls_currentConfirmedCount.append(currentConfirmedCount)
    x = np.array(ls_province)
    y = np.array(ls_currentConfirmedCount)
    plt.title("国内当前确诊人数")
    plt.xlabel("省份")
    plt.ylabel("人数")
    for i,j in zip(range(len(y)), y):
        # print(i,j,j)
        plt.text(i, j, j)#(i,j)表示添加标签的位置，j表示添加的内容
    plt.bar(x, y)
    plt.show()

# 分析疑似病例：
def yszzt():
    # 绘制疑似病例柱状图
    ls_province = []  # 省份
    ls_suspectedCount = []  # 疑似病例
    for x in ls:
        provinceName = x["provinceShortName"]
        suspectedCount = x["suspectedCount"]
        ls_province.append(provinceName)
        ls_suspectedCount.append(suspectedCount)
    x = np.array(ls_province)
    y = np.array(ls_suspectedCount)
    plt.title("国内疑似病例人数")
    plt.xlabel("省份")
    plt.ylabel("人数")
    for i,j in zip(range(len(y)), y):
        plt.text(i, j, j)#(i,j)表示添加标签的位置，j表示添加的内容
    plt.bar(x, y)
    plt.show()

def qzbzt():
    # 绘制当前确诊饼图
    ls_province = []  # 省份
    ls_currentConfirmedCount = []  # 当前确诊
    for x in ls:
        provinceName = x["provinceShortName"]
        currentConfirmedCount = x["currentConfirmedCount"]
        ls_province.append(provinceName)
        ls_currentConfirmedCount.append(currentConfirmedCount)

    plt.pie(ls_currentConfirmedCount,
            labels = ls_province,
            autopct = "%.0f%%"
           )
    plt.title("国内当前确诊饼图")
    plt.show()

def ysbt():
    # 绘制疑似病例饼图
    ls_province = []  # 省份
    ls_suspectedCount = []  # 疑似病例
    for x in ls:
        provinceName = x["provinceShortName"]
        suspectedCount = x["suspectedCount"]
        ls_province.append(provinceName)
        ls_suspectedCount.append(suspectedCount)

    plt.pie(ls_suspectedCount,
           labels = ls_province,
           autopct = "%.0f%%")
    plt.title("国内疑似病例统计")
    plt.show()

def zfxzzt():
    # 绘制中风险地区柱状图
    ls_province = [] # 省份
    ls_midDangerCount = [] # 中风险地区
    for x in ls:
        provinceName = x["provinceShortName"]
        midDangerCount = x["midDangerCount"]
        ls_province.append(provinceName)
        ls_midDangerCount.append(midDangerCount)
    province = np.array(ls_province)
    midDangerCount = np.array(ls_midDangerCount)
    plt.title("国内中风险地区柱状图")
    plt.xlabel("省份")
    plt.ylabel("中风险地区个数")
    for i,j in zip(range(len(midDangerCount)), midDangerCount):
        plt.text(i, j, j)#表示添加标签的位置，j表示添加的内容
    plt.bar(province, midDangerCount)
    plt.show()
#
print('按1查看当前确诊柱状图 按2查看疑似病例柱状图 按3查看当前确诊饼图 按4查看疑似病例饼图 按5查看中风险地区柱状图 ')
n=input('请输入:')
while n!='0':
    if n=='1':
        qzzzt()
        print('查看成功')
    elif n=='2':
        yszzt()
        print('查看成功')
    elif n == '3':
        qzbzt()
        print('查看成功')
    elif n == '4':
        ysbt()
        print('查看成功')
    elif n == '5':
        zfxzzt()
        print('查看成功')
    n = input('请输入:（按0退出）')