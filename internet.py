#網路連線
#載入模組
import json
import urllib.request as request
# src="https://tietunghuat.github.io/myresume/"
# with request.urlopen(src)as response:
#     data=response.read().decode("utf-8")
# print(data)

# ########################
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src)as response:
    data = json.load(response)   #利用json格式來讀取
print(data)
#取得公司名稱，並列表出來
clist = data["result"]["results"] #我要result裡面的results的公司名稱的公司地址 ，result是第一次，results是第二層
print(clist)
for company in clist:
    print(company["公司名稱"])
for address in clist:
    print(address["公司地址"])

with open("data/government.txt", mode="w", encoding="utf-8") as file:
    for company in clist:
     file.write(company["公司名稱"]+"\n")
