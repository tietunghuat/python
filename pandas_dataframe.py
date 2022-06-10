import pandas as pd
data=pd.DataFrame({"name":["Lebron","Harden","Russell"],"jersey":[23,13,0]},index=["a","b","c"])
print(data)
print(data.iloc[1]) #.iloc是利用dataframe來找值
print("===================")
print(data.loc["a"])  #.loc是利用index索引來找值
print("===================")
print(data["name"])

print("資料數量:", data.size)
print("資料形狀（列，欄）:", data.shape)
print("資料索引:",data.index)
print("取得第三列:", data.iloc[2], sep="\n") #sep="\n" 換行的意思
print("===================")
print("取得第二列",data.loc["b"], sep="\n")  # .loc是利用index索引來找值
print("===================")
print("取得名字", data["name"], sep="\n")

all=data["name"]
print("全部變大寫",all.str.upper(),sep="\n")

number=data["jersey"]
print("平均值",number.mean())

#建立新的欄位,並跟上面加在一起， 兩個方法都可以用，第一個比較適合
data["team"]=["Lakers","Nets","Washington"]
data["money"]=[80000,70000,50000]
data["rank"]=pd.Series([1,2,8],index=["a","b","c"])  #利用單維度來增加欄位，比較正式
data["cp"]=data["rank"] #可以直接duplicate
data["salary"]=data["money"]/data["cp"] #直接計算
print(data)