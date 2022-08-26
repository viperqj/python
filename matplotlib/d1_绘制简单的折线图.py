import matplotlib.pyplot as plt
import pandas as pd
s=pd.date_range(start='2022-08-02',freq='D',periods=10)
df=pd.DataFrame(data=[30,29,33,38,28,26,31,24,19,25],index=s,columns=['温度'])
x=s
y=df['温度']
plt.plot(x,y)
plt.show()