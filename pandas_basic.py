#pandas列表
#series 單維度
#dataframe雙維度
import pandas as pd
data=pd.Series([20,15,28])
print(data)
print("----------------------------")
print("max:",data.max())
print("median:",data.median())
print("min:", data.min())
print("----------------------------")
#全部乘2
sum=data*2
print(sum)
print("----------------------------")
#全部做比較
compare=data==15  #如果data列表有15的話為true
print(compare)
print("----------------------------")
#建立dataframe
dic=pd.DataFrame({"name":["KD","James","Kevin"],"number":[7,23,0]})
print(dic)
print("----------------------------")
print(dic["name"]) #就只會取得name的欄位
print("----------------------------")
print(dic.iloc[1])  #取得第一列，1等於第二列，0是第一列
