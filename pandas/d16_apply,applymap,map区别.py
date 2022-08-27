import pandas as pd
# apply()和applymap()可以用在Series,对series每个元素都执行一次函数;也可以用于dataframe，作用于某一列或者是某一行,或每个元素
s=pd.Series(data=[10,20,30,40],index=['a','b','c','d'])
print(s)
s=s.apply(lambda x:x+10)
print(s)
print('------------------------------------------------------------------')
f=pd.DataFrame(data=[[1,2,3],[5,6,7],[8,9,10]],index=['a','b','c'],columns=['A','B','C'])
print(f)
f=f.apply(lambda x:x+1)
print(f)
print('------------------------------------------------------------------map只可以用在Series')
o=pd.DataFrame(data=[['nan'],['nv'],['nan']],columns=['性别'])
print(o,'\n')
def aa(x):
    if x=='nan':
        return 'male'
    else:
        return 'female'
o=o['性别'].map(aa)
print(o)
print('--------------------------参数可以为字典')
o=o.map({'male':'男','female':'女'})
print(o)

