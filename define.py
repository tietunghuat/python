def say(msg):
    print(msg)
    return
say("I'm Jabez")
    
def multiply(j,k):
    print("j*k:",j*k)
    return
multiply(10,10)
multiply(50,10)


def divide(o,p):
    print("o / p :",o/p)
    return  10
# 但divide(10,2)傳上去divide(o,p),value = divide(10, 2)的divide(10, 2)就會變 0 or none，所以return 後面的東西是return回給value的
value = divide(10, 2)
print(value)    # 等於 none

def add(n1,n2):
    result=n1+n2
    return result
niu=add(5,7)  #呼叫函式 return好add(5,8)就是13
print("5+7:",niu)

def times(a,b):
    total=a*b
    return total
hi=times(5,8)
print("5*8:",hi)


def plus(q,w):
    subtotal=q+w
    return subtotal
number=plus(1,3)+ plus(5,5)
print("number",number)

#函式用來做 包裝 同樣程式可以重複利用
def cal(min,max):
    sum=0
    for x in range(min,max):
        sum=sum+x
    print(sum)
    return sum
value = cal(1, 55)+cal(22, 33)
print("Value:",value)
cal(1, 55)
cal(22, 33)
