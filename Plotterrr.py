import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x =  np.linspace(0, 10, 20)
y = x*x
z = x+y
# print(x)
print(type(plt.plot(x, y)))
plt.xlabel("x-axis") #labeling x axis
plt.ylabel("y-axis") #labeling y axis