import pandas as pd
import random
s=pd.DataFrame(data=[[random.random() for i in range(0,3)],[random.random() for i in range(0,3)],[random.random() for i in range(0,3)]],columns=['A','B','C'])
s1=s
print(s)
#           A         B         C
# 0  0.029794  0.302089  0.341501
# 1  0.656455  0.619762  0.562606
# 2  0.893295  0.621536  0.911135
s=s.round(4)
print(s)
#       A     B     C
# 0  0.51  0.68  0.51
# 1  0.48  0.37  0.33
# 2  0.74  0.95  0.98
print('-------------------------------------------------------------指定列')
s=s.round({'A':2,'B':3})
print(s)
#       A      B       C
# 0  0.14  0.281  0.3598
# 1  0.17  0.442  0.5711
# 2  0.84  0.273  0.5447
print('-------------------------------------------------------------自定义函数')
s1=s1.applymap(lambda x:'{:.2f}'.format(x))
print(s1)






















