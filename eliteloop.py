#break寫法
#如果n不等於3 繼續執行
#如果迴圈執行到3，直接停止並顯示
n=1
while n<5:
    if n==3:
        break #如果if true，停止if迴圈
    print("first:",n)
    n+=1
print("last:",n)

#continue寫法 if continue=True 忽略下面所有
#if continue=False執行continue下面所有
z=0
for x in [2,3,4,5,6,7,8]:
    if x % 2 ==0:
        continue   #if x%2==0 is true ,執行continue，continue就是直接重新跑迴圈不理會這個迴圈樓下的
    print("x:",x)
    z +=1    #因為 2,4,6,8%2==0，所以會執行到這裡
print("z:",z)


#while/else迴圈
m=1
while m<5:
    print("Var:",m)
    m+=1
else:
    print("last:",m) #先跑完else再結束迴圈

#for/else迴圈
for c in "hello":
    print("All the string:",c)
else:
    print(c) #印最後一個

#for/else迴圈
total =0
for k in range(5):
    total+=k
else:
    print("Total:",total)

#開根號
op=int(input("請輸入數字:"))
for i in range(op):
    if i*i==op:
        print("平方根:",i)
        break #強制結束不會跑else
else:
    print("沒有平方根")
