#封裝裡的變數和函式，為‘類別的屬性’
#實體物件
class Test:
    x=3    #變數
    
    def say():  # 函式
        print("hello")

Test.x+3
Test.say()

class source:
    #變數一
    src=["King","JAmes"]
    #函式二
    # a=input("請輸入名字：")
    def read(a):
        #如果丟進去的資料不再source裡面，就不支援
        if a not in source.src:
            print("Not support")
        else:
            print("Read from", a)


print(source.src)
source.read("KingJabez")
source.read("King")


#######################
class nba:
    player=["KD","Lebron","Harden"]
    def member(a):
        if a not in nba.player:
            print("Not attempted")
        if a  in nba.player:
            print("Attempted")
print(nba.player)
cc=nba.member("King james")
bb=nba.member("Harden")
