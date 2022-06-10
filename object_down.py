#實體方法 是 在實體物件中的函式
class point:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    #定義實體方法 
    #實體方法一
    def show(self):
        print(self.x,self.y)
        #實體方法二
    def distance(self,k,o):
        return (((self.x-k)**2)+((self.y-o)**2))**0.5
p=point(1,5)
p.show() #呼叫實體方法
q=p.distance(5,3)
print("q:",q)


#########################
#包裝的概念，就是簡化的意思，清楚
class file:
    def __init__(self,op):
        self.name=op
        self.file=None #尚未開啟，初期是none
    def open(self):#這邊利用來開file
        self.file=open(self.name,mode="r",encoding="utf-8")
    def read(self):
        return self.file.read()
#第一個檔案
f1=file("data/data1.txt")
f1.open()
data=f1.read()
print(data)
#第二個檔案
f2 = file("data/data2.txt")
f2.open()
data2 = f2.read()
print(data2)
