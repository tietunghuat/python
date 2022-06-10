#利用python創造網址
from flask import Flask
app=Flask(__name__) #__name__代表目前知情的模組


@app.route("/") #decorator 函式的裝飾 
def home():
    return "Hello Flask 2"

@app.route("/test")  #加在127.0.0.1:5000/後面的裝飾 #如果交給/test，給def test()處理
def test():
    return "This is Test" 
 
@app.route("/king")#127.0.0.1:5000/king
def king():
    return "Hello Laker Nation!"
if __name__=="__main__":  #如果以主c程式
    app.run() #立刻啟動伺服器