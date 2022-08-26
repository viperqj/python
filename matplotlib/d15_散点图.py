import matplotlib.pyplot as plt
import random
x=[i for i in range(1,11)]
y=[random.randint(1,11) for i in range(1,11)]
plt.scatter(x,y,color='r')
plt.show()