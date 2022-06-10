#抓取ppt網頁原始碼(HTML)
import urllib.request as req
url = "https://www.ptt.cc/bbs/Nethood/index.html"
#建立一個request物件，附加request headers的資訊
#讓explorer認為我們是普通人
request = req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)    #把W網頁的html資料印出來


import bs4
root=bs4.BeautifulSoup(data,"html.parser")  #必須寫的bs4 程式碼
titles=root.find("div",class_="title") #搜尋條件
print(titles.a.string) #抓到標題內容  ,titles是div，a是href，string才是內容
whole = root.find_all("div", class_="title")  # 搜尋所以想要的
print(whole)  # 抓到想要的
for title in whole:
    if title.a !=None:   #如果title的a裡面不是空的，是有值得話，全部print出來
        print(title.a.string)

#抓title，然後再抓裡面的文字
print(root.title.string)
