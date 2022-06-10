import pandas as pd
data=pd.Series([20,15,30,50,-32],index=["a","b","c","d","e"])#建立自己的索引
print(data)
print("資料形態:",data.dtype)
print("資料數量:",data.size)
print("資料索引:",data.index)
print("Data num:",data[1]) 
print("根據索引取得資料",data["c"])
print("=======================")
print("=======================")
print("最大值:", data.max())
print("綜合:",data.sum())
print("標準差:",data.std())
print("中位數:",data.median())
print("最大的前三個數:\n",data.nlargest(3))
print("=======================")
source=pd.Series(["Python","Java","HTML","Css"])
print("全部變小寫字體\n",source.str.lower())
print("最大的前三個數:\n", data.nlargest(3))
print("=======================")
print(source.str.len()) #算出每個字串的長度
print(source.str.cat(sep=" - ")) #把字串串起來
print(source.str.contains("P")) #查詢看有沒有大寫的P字串，沒有就false
print(source.str.replace("Java","PHP")) #取代上面