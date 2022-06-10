def say(msg="hello"):
    print(msg)
say("hello function")
say()  #如果沒有放函式資料，會顯示預設的資料"hello"


def plus(a,b):
    result=a+b
    print(result)
plus(b=5,a=2) #倒過來沒關係 不管順序
plus(3,2)

#無限長度的參數
def message(*content):
     for abc in content:
         print(abc)
message("yo","Lebron","Goat")

def power (base,exp=0): #如果沒有給值顯示預設
    print("base^exp:",base**exp)
power(3,2)
power(4)  # 如果沒有給值顯示預設 4^ 0 =1

#無限長度的參數
def niu(*low):
    total=0
    for gg in low:
        total=total+gg
    print("average:", total/len(low))  # total除 niu的長度，有兩個就是 2
niu(2,3)
niu(5,10)
niu(8,4,3,5)


