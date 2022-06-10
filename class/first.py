a=int(input("Please insert your weight:"))
b = int(input("Please insert your height:"))
c= (a/(b*b))*10000
if c < 18.5:
    print("underweight")
elif c < 24.9:
    print("normalweight")
elif c <29.9:
    print("overweight")
else:
    print("obesity")
print("your bmi =",round(c,2))
