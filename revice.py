s="King"*3
print(s)

z=1
while z<=5:
    print(z,"Z is <=5")
    z+=1

z = 1
while z <= 5:
    print(z, "Z is <=5")
    z+=1
    if z==4:
        break
   
y=1
for y in [2,3,4,5,6,7,8,9]:
    if y%2==0:
        y += 1
        continue
    print("y is ",y)
print("the last number of y is ",y)


# x=int(input("Please insert number:"))
# for a in range(x):
#     if a*a==x:
#         print("平方根是:",a)
#         break
# else:
#     print("Invalid number")

def cal(a,b):
    print("The number of a*b is :",a*b)
cal(1,3)

def sa(x,y):
    total=x+y
    return total
value=sa(5,8)+sa(3,9)
print("the value is:",value)

def no(*a):
    for x in a:
        print(x)
no("Lebron","king","James")

def aa(c,d=0):
    print("c^d:",c**d)
aa(5,3)
aa(3)

import sys
sys.path.append("modules")

import geometry as g
result=g.distance(5,1,9,8)
print("The result is:",result)
another=g.slope(7,9,2,1)
print("The slope is:",another)

import packet.line as line
result=line.len(5,1,9,8)
print("The line is:",result)

import packet.point as point
dk=point.distance(1,9)
print("The distance is:",dk)

class source:
    data=["King","Jabez","Ethel"]
    def message(a):
        if a in source.data:
            print("Attempt")
        else:
            print("False")
source.message("Jabez")
source.message("Lebron")

class other:
    def __init__(self):
        self.x =3
        self.y =4
k=other()
print(k.x)


class other:
    def __init__(self,o,p):
        self.x = o
        self.y = p

k = other(5,3)
print(k.x+k.y)


class other:
    def __init__(self):
        self.a = "KIng"
        self.b = "James"


k = other()
print(k.a+k.b)


class other:
    def __init__(self,x,y):
        self.a = x
        self.b = y


k = other("Wahaha","Muahaha")
a = other("Maggot", "Noob")
print(k.a,",",k.b)
print(a.a,",",a.b)

class new:
    def __init__(self,x,y):
        self.a = x
        self.b = y
        
    def show(self):
        print(self.a,",",self.b)
    def ha(self,k,o):
        self.c=k
        self.d=o
        print(self.a+self.c)
        print(self.a+self.b+self.c+self.d)
e=new(1,2)
e.show()
e.ha(5,8)

with open("folders/next.txt",mode="w",encoding="utf-8") as file:
    file.write("Hi ,ethel siao!")

with open("folders/next.txt",mode="r",encoding="utf-8") as file:
    noo=file.read()
print(noo)

sum=0
with open("folders/num.txt", mode="r", encoding="utf-8") as number:
    for x in number:
       sum+=int(x)
print(sum)

import json
with open ("json/config.json",mode="r",encoding="utf-8") as file:
    data=json.load(file)
print(data)
print(data["name"])
data["name"]="King JAmes"
print(data["name"])

with open("json/config.json", mode="w", encoding="utf-8") as file:
    json.dump(data,file)

import urllib.request as request
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as website:
    data=json.load(website)
# print(data)
# list=data["result"]["results"]
# for name in list:
#     print(name["公司名稱"])
# for name in list:
#     print(name["公司地址"])
# with open("data/company.txt",mode="w",encoding="utf-8") as company:
#     for name in list:
#         company.write(name["公司名稱"]+"\n")

# with open("data/address.txt",mode="w",encoding="utf-8") as address:
#     for add in list:
#         address.write(add["公司地址"]+"\n")

import pandas as pd
data=pd.Series(["James","KD","Irving"])
print(data)

number = pd.DataFrame({"name": ["KD", "James", "Kevin"], "number": [7, 23, 0]})
print(number)

import urllib.request as req
url = "https://www.ptt.cc/bbs/Nethood/index.html"
req = req.Request(
    url, headers="user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
with req.urlopen(request) as data:
    print(data)