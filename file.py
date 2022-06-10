#儲存檔案
# 檔案物件=open(檔案路徑，mode=開啟模式)
#開啟模式
 #讀取模式 - r
 #寫入模式 - w
 #讀寫模式 - r+
file = open("folders/data.txt", mode="w", encoding="utf-8")  # 開啟
file.write("你好python,HELLO FILE \nSecond")  # 操作
file.close()  # 關閉

#寫入文字
#檔案物件.write(字串)

#寫入換行符號
#檔案物件.write("King is goat\n")

#寫入 JSON 格式
#import json
import json
with open("json/config.json",mode="r",encoding="utf-8") as file:
    data=json.load(file)
print(data) #還未改字典
print("team:",data["team"])
data["name"]="Lebron James" #改了字典之後



#json.dump(要寫入的資料，檔案物件)
#修改之後寫回檔案
with open("json/config.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file)

#關閉檔案
#檔案物件.close()

#最佳實務 , 這個會自動關閉，不用 .close()
# with open(檔案路徑,mode=開啟模式) as 檔案物件:
# 讀取或寫入檔案的程式
with open("folders/first.txt",mode="w",encoding="utf-8") as file:
    file.write("詹姆斯第一人 \n湖人總冠軍!")

#讀取檔案
with open("folders/first.txt",mode="r",encoding="utf-8") as file:
        data=file.read()
print(data)

#做加法
with open("folders/num.txt", mode="w", encoding="utf-8") as number:
    number.write("2\n 5 \n 3 \n 8")

#讀取檔案
sum=0
with open("folders/num.txt", mode="r", encoding="utf-8") as number:
    for x in number:
        sum+=int(x)
print(sum)
