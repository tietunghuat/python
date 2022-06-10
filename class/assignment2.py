import pandas as pd
data=pd.read_csv("data.csv")
print(data)

import matplotlib.pyplot as plt

import numpy as np 
colors = np.array(["red","blue","green"])
groups=[0,0,0,2,0,2,1,2,1,2,1,1]

plt.scatter(data.X,data.Y,c=colors[groups])
plt.show()

from sklearn.cluster import KMeans

model = KMeans(n_clusters=2).fit(data)

plt.scatter(data.X,data.Y,c=colors[model.labes_])
plt.show()

test=[[3,4],[5,7],[10,12]]
print(model.predict(test))



