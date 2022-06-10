#載入模組
#import random

#隨機選取
import random
#隨機選取一個資料
print("隨機選1:",random.choice([0,1,5,8]))
#隨機選取兩個資料
print("隨機選2:",random.sample([0, 1, 5, 8],2))

#隨機調換順序
data=[5,8,4,2]
b=random.shuffle(data)
print("shuffle:",b)

#隨機亂數
#去0.0 ~ 1.0的隨機亂書
#uniform=隨機出現幾率相同
print("random uniform:",random.uniform(0, 8))

#0 ~ 1之間的亂數
total=random.random()
print("total:",total)

#常態分配
#在100-10=90,100+10=110 ,90~110之間去亂數
print("常態分配:",random.normalvariate(100,10))


import statistics as stat
#統計
#平均數
print("mean:", stat.mean([5, 8, 7, 9]))
#中位數
print("medium:", stat.median([5, 8, 7, 9]))
#標準差
print("stdev:", stat.stdev([5, 8, 7, 9]))




