#抓取ppt網頁原始碼(HTML)
import bs4
import urllib.request as req
def getData(url):
    #建立一個request物件，附加request headers的資訊
    #讓explorer認為我們是普通人
    request = req.Request(url, headers={
                        "cookie": "over18=1",
                        "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"})

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    print(data)

    root = bs4.BeautifulSoup(data, "html.parser")
    whole = root.find_all("div", class_="title")  # 搜尋所以想要的
    #抓title，然後再抓裡面的文字
    print(root.title.string)
    print(whole)  # 抓到想要的
    for title in whole:
        if title.a != None:
            print(title.a.string)
    #抓取上頁的原始碼

    nextLink=root.find("a",string="‹ 上頁")
    print(nextLink)
    return nextLink["href"]

page = "https://www.ptt.cc/bbs/Gossiping/index.html"

nice=getData(page) #讀取
print(nice)

count=0
while count<5:
    page = "https://www.ptt.cc/"+getData(page)
    count+=1
