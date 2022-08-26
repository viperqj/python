#索引  .index
# 显示所有列名称 .columns
# 显示所有的值 .values
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.rcParams['font.sans-serif'] = ['KaiTi']
# 1. 准备数据
# 1.1 加载数据
datas = pd.read_csv('世界各国疫情数据.csv')
# 1.2 准备折线图需要的数据
# 日期, 作为横轴的刻度
x_ticks = datas['dateId'].values
# print(type(x_ticks))==<class 'numpy.ndarray'>——》[20200119 ... 20220702]
# x轴的数据
x = list(range(x_ticks.shape[0])) #x_ticks.shape=(896,)  x_ticks.shape[0]=896
# y轴
# 中国现有确诊病例数量
china = datas['中国'].values  #<class 'numpy.ndarray'>
# 美国现有确诊病例数量
usa = datas['美国'].values #<class 'numpy.ndarray'>
# print(x_ticks)
# print(x)
# print(china)
# print(usa)

# 2. 创建画布
fig = plt.figure(figsize=(10, 6), dpi=100) #dpi 清晰度
# 3. 初始化折线图和坐标轴的范围与刻度
# 3.1 定义变量, 用于记录每一帧折线图显示的数据条数
line_range = 8
# 3.2 定义变量, 用于记录每一帧x轴刻度的数量
xticks_range = 10
# 3.3 初始化中美折线图对象
china_line, = plt.plot([], [], color='r', marker='o', label='中国')
usa_line, = plt.plot([], [], color='g', marker='*', label='美国')

# 3.4 显示图例
plt.legend()
# 初始化
# 3.5 设置x轴,y轴的范围以及x轴的刻度
plt.ylim(0, max(usa))
plt.xlim(0, line_range)
plt.xticks(x[0: xticks_range], x_ticks[0: xticks_range])


# 4. 实现动画的更新方法
def update(i):
    # 更新折线图数据
    start = 0 if i - line_range + 1 < 0 else i - line_range + 1
    end = i + 1
    # 更新中国折线图数据
    china_line.set_data(x[start: end], china[start: end])
    # 更新美国折线图数据
    usa_line.set_data(x[start: end], usa[start: end])

    # 设置x轴的范围和刻度
    if i >= line_range:
        xticks_end = end + 2
        # 更新x轴范围
        plt.xlim(start, xticks_end)
        # 更新x轴刻度
        plt.xticks(x[start: xticks_end], x_ticks[start: xticks_end])

    return china_line, usa_line


# 5. 创建动画对象
animation = FuncAnimation(fig, update, frames=x, repeat=False)
# update(10)
# 6. 展示
plt.show()