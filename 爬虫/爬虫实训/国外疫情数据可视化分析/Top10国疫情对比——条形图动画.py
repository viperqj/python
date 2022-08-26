import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.sans-serif'] = ['KaiTi']
# 1. 准备数据
# 1.1 加载数据                          ⽤index_col=0，直接将第⼀列作为索引
# --------------------------------------------------------
datas = pd.read_csv('世界各国疫情数据.csv', index_col=0, dtype=np.int32)
# 1.2 准确累计确诊病例数量前10的国家疫情信息
top10 = datas.iloc[4:,:10]# 根据序列iloc# 获取特定位置的值 行索引列索引从0开始
# iloc[a:b,c:d]:取行索引从a到b-1，列索引从c到d-1的数据

#绑定国家与颜色
color=['r', 'g', 'b', 'm', 'c', 'yellow', 'orange', 'yellowgreen', 'hotpink', 'gold']
name_color_map=dict(zip(top10.columns,color))
# print(name_color_map)
# {'美国': 'r', '印度': 'g', '巴西': 'b', '法国': 'm', '德国': 'c', '英国': 'yellow', '意大利': 'orange', '俄罗斯': 'yellowgreen', '韩国': 'hotpink', '土耳其': 'gold'}

# 2. 创建画布和绘图区
fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

# 3. 实现动画更新方法
def update(date):
    # 1. 绘制基本的条形图
    # 清空画布
    ax.clear()
    # 3. 对条形图按现有确诊人数降序排序
    data = top10.loc[date].sort_values()#data是指定行的数据
    print(data)
    # 绘制条形图
    color=[name_color_map[name] for name in data.index]
    ax.barh(data.index, data.values,color=color
            )

    # 2. 添加辅助信息
    # 2.1 在每一个柱状体上添加国家和现有确诊病例数量
    # enumerate函数⽤于将⼀个可遍历的数据对象(如列表、元组或字符串)组合为⼀个索引序列，同时列出数据和数据下标
    for i, name in enumerate(data.index):
        # 获取这个国家现有确诊病例数量
        value = data[name]
        # print(i, name, value)
        dx = data.max() / 100  # 宽度的百分之一间隔
        # 现有确诊病例数量
        ax.text(value + dx, i, value, fontsize=12)
        # 国家名称
        name_x = value - len(name) * dx * 2.5
        if name_x > 0: #如果国家名字显示在框外，则不添加
            ax.text(name_x, i, name, fontsize=12)

    # 2.2 添加日期 transform=ax.transAxes 转换刻度（0,1）
    ax.text(0.8, 0.3, date, transform=ax.transAxes, fontsize=16)
    # 2.3 设置x的刻度在顶部
    ax.xaxis.set_ticks_position('top')
    # 2.4 添加标题
    ax.text(0, 1.06, '现有确诊病例数量', transform=ax.transAxes, fontsize=14)
    ax.text(0.4, 1.12, 'Top10国疫情对比', transform=ax.transAxes, fontsize=18)
    # 2.5 显示网格(x轴)
    ax.grid(axis='x')
    # 2.6 不显示边框
    plt.box(False)


# update(top10.index[60])
# 4. 创建动画并展示                       top10.index就是索引（日期）
animation = FuncAnimation(fig, update, frames=top10.index, repeat=False)
plt.show()

# FuncAnimation是Matplotlib库为我们提供的用于绘制动态图像的接口
# fig：画布对象，由创建画布时的返回得到
# frames:动画长度，一次循环包含的帧数
# frames的参数值是一个值序列，每调用一次回调函数就从中取一个值传递给update


