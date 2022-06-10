import urllib.request as req
url = "https://www.ptt.cc/bbs/Nethood/index.html"
request=req.Request(url, headers={"user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"})
with req.urlopen(request) as data:
    hi=data.read().decode("utf-8")
print(hi)

import bs4
root=bs4.BeautifulSoup(hi,"html.parser")

whole = root.find("div", class_="title")
print(whole.a.string)

entire=root.find_all("div",class_="title")
print(entire)

for title in entire:
    if title.a != None:
        print(title.a.string)
