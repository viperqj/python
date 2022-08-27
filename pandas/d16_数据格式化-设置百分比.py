import pandas as pd
import random
s=pd.DataFrame(data=[[random.random() for i in range(0,3)],[random.random() for i in range(0,3)],[random.random() for i in range(0,3)]],columns=['A','B','C'])
print(s)
print('----------------------------------------------------------------------apply()')
s['A的百分比']=s['A'].apply(lambda x:format(x,'.0%'))
print(s)
#           A         B         C A的百分比
# 0  0.227958  0.727614  0.095694   23%
# 1  0.036354  0.950447  0.337934    4%
# 2  0.180501  0.815429  0.390856   18%
print('----------------------------------------------------------------------map()')
s['A的百分比']=s['A'].map(lambda x:format(x,'.0%'))
print(s)