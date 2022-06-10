#類別建立實體物件，實體屬性
#實體屬性
class point:
    def __init__(self): #定義初始化函式
        self.x=3 #實體屬性
        self.y=4 #實體屬性
p=point() #產生建立實體物件放進變數
print(p.x,",",p.y) #實體物件.屬性名稱


class tie:
    def __init__(self,a,b):
        self.x = a #實體屬性
        self.y = b #實體屬性
p = tie(1,5)
p1=tie(5,8)
print(p.x,",", p.y)
print(p.x + p.y)
print("點到點:",(p.x+p.y)+(p1.x+p1.y))


class fullname:
    def __init__(self):
        self.first="king"
        self.second="james"
a1=fullname()
print(a1.first,",",a1.second)


class fullname:
    def __init__(self,a,b):
        self.first = a
        self.second = b


a1 = fullname("Lebron","James")
print(a1.first, ",", a1.second)


