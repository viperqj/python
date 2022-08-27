import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
s=pd.DataFrame(data={
    '商品名':['小米手机','华为手机','华为电脑','小米电脑'],
    '北京销量':[400,200,50,60],
    '上海销量':[99,888,7,1],
    '广州销量':[999,88,11,2],
    '天津销量':[10,500,3,22],
    '苏州销量':[10,70,88,77],
    '沈阳销量':[99,9,8,33],
})
print(s)
dict1={
    '北京销量':'华北地区',
    '上海销量':'华东地区',
    '广州销量':'华南地区',
    '天津销量':'华北地区',
    '苏州销量':'华东地区',
    '沈阳销量':'华北地区'
}
s1=s.groupby(dict1,axis=1).sum()
print(s1)

print('--------------------------------------------------------------------------')

p=pd.Series(dict1)
s1=s.groupby(p,axis=1).sum()
print(s1)























