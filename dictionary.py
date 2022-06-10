#字典
s={3,4,5}
print(6 not in s)

#交集
s1={3,4,5}
s2={4,5,6}
s3= s1&s2
print("交集:", s3)

#聯集
s1 = {3, 4, 5}
s2 = {4, 5, 6}
s3 = s1 | s2
print("聯集:", s3)

#差集
s1 = {3, 4, 5}
s2 = {4, 5, 6}
s3 = s1 - s2
print("差集:", s3)

#反交集
s1 = {3, 4, 5}
s2 = {4, 5, 6}
s3 = s1^s2
print("反交集:",s3)

#set(字串)
s=set("Hello")
print(s)
print("H" in s)

#字典dictionary, "lebron"是key,"詹姆斯"是value
dic={"jabez":"同發","lebron":"詹姆斯","curry":"庫里"}
dic["jabez"]="池同發"
print(dic["jabez"])
print("kyrie" not in dic)
del dic["curry"]
print(dic)

#從列表資料產生字典 [2,3,4]是列表資料 x:x*2是字典
dic={x:x*2 for x in [2,3,4]}
print(dic)
