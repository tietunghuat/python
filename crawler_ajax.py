#AJAX是先取得沒有資料的html網頁，然後再ajax技術去取得剩下資料，再顯示出來


import urllib.request as req
url = "https://medium.com/_/graphql"
#建立一個request物件，附加request headers的資訊
#讓explorer認為我們是普通人
request = req.Request(url, headers={
                      "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
print(data)


import json

data=json.load(data)
print(data)
#取得json資料中的文章標題
posts=data["data"]["modules"]["2"]["feedItems"]
for key in posts:
    post=posts[key]
    print(post["title"])
