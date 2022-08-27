# 1 describe() 查看每列的统计汇总信息,DataFrame类型
# 2 count() 返回每一列的非空值的个数
# 3 sum() 返回每一列的和，无法计算返回空值
# 4 max() 返回每一列的最大值
# 5 min() 返回每一列的最小值
import pandas as pd
data={
    '名称':['小太阳','剪刀','电脑'],
    '价格':[150,15,999],
    '数量':[99,999,888],
    '供应商':'英雄联盟'
}
s=pd.DataFrame(data=data)
print(s)
#     名称   价格   数量
# 0  小太阳  150   99
# 1   剪刀   15  999
# 2   电脑  999  888
print('------------# 1 describe() 查看每列的统计汇总信息,DataFrame类型')
print(s.describe())
print('------------# 2 count() 返回每一列的非空值的个数---------------')
print(s.count())
print('------------# 3 sum() 返回每一列的和，无法计算返回空值----------')
print(s.sum())
print('------------# 4 max() 返回每一列的最大值----------------------')
print(s.max())
print('------------# 5 min() 返回每一列的最小值----------------------')
print(s.min())