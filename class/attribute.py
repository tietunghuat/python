import random
class Coin:
    value =1
    face ="head"
    def __init__(self,v=None):
        if v==None:
            self.value=5
        else:
            self.value=10
    def getFace (self):
        return self.face
    def showValue(self):
        print(self.value)
    def setValue(self,v):
        self.value=v
    def flip(self):
        if random.randint(0,1)==0:
            self.face="headtwo"
        else:
            self.face="tail"

mycoin1= Coin()
mycoin2=Coin(10)

for i in range(5):
    mycoin1.flip()
    mycoin2.flip()
    print(i,"coin1:",mycoin1.getFace(),"coin2:",mycoin2.getFace())