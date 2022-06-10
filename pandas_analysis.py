import pandas as pd
#讀取資料，讀取CSV的檔案
data=pd.read_csv("googleplaystore.csv")
# print(data)
print("資料數量",data.shape)  #10841筆資料，13個欄位
print("資料欄位", data.columns)
print("======================")
print(data["Rating"])  #找出rating欄位的所有
condition = data["Rating"] < 4  # 找出大於4的欄位
filteredData = data[condition]
print(filteredData)
print("平均數",data["Rating"].mean())
print("中位數",data["Rating"].median())
print("前100的平均",data["Rating"].nlargest(100).mean())
print("======================")

#分析資料，把資料轉換成數字，再覆蓋回來
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free",""))#把符號跟Free替換掉
print(data["Installs"]) #先把上面有錯的符號，跟string替換掉再出現
condition_data=data["Installs"]>100000
print("找出大於100000的程式",data[condition_data].shape[0]) #(4950,13) 4950是第0個，所有把0顯示出來
print("======================")
#尋找關鍵字
keyword=input("Please insert keyword:")
condition_keyword = data["App"].str.contains(keyword, case=False)  # case=False 是忽略大小寫的意思
print("尋找關鍵字",data[condition_keyword])
print("尋找關鍵字的數量", data[condition_keyword].shape) #(有多少筆，有多少欄位)
