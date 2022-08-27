# 1 values 查看所有元素的值
# 2 dtypes 查看所有元素的类型
# 3 index 查看所有行名、重命名行名
# 4 columns 查看所有列名、重命名列名
# 5 T 行列数据转换
# 6 head 查看前N条数据,默认5条
# 7 tail 查看后N条数据,默认5条
# 8 shape 查看行数和列数shape[0]表示行,shape[1]表示列
# 9 info() 查看索引、数据类型和内存信息
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
print('--------------------------------------------')
print(s.head(2))
print('--------------------------------------------')
print(s.tail(2))
print('--------------------------------------------修改行索引')
s.index=[7,8,9]
print(s)
print('--------------------------------------------修改列索引')
s.columns=['name','price','num','supply']
print(s)
print('------  shape 查看行数和列数shape[0]表示行,shape[1]表示列')
print(s.shape)
print(s.shape[0])
print(s.shape[1])
print(s.info())