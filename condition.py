#判斷式
if True:
    print("Suns champion")
else:
     print("Bucks champion")
#輸入
x=input("請輸入數字:")
x=int(x) #轉換成int形態
if x > 200:
    print("The no is > 200")
elif x>100 :
    print("The no is > 100")
else:
    print("The no is invalid")

#輸入進階 四則運算
x1=int(input("請輸入數字1:"))
x2=int(input("請輸入數字2:"))
x3= x1+x2
print(x3)

#輸入進階 四則運算 判斷
ex=input("請輸入運算:+,-,*,/ :")
if ex == "+" :
    print(x1+x2)
elif ex == "-":
    print(x1-x2)
elif ex== "*":
    print(x1*x2)
elif ex=="/":
    print(x1/x2)
else:
    print("請輸入運算式")


abc=int(input("Please insert number:"))
print(abc)
if abc > 100:
    print("Suns win")
elif abc>50:
    print("Bucks win")
else:
    print("tied")