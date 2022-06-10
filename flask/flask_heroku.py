#step 1:描述Python環境 runtime.txt
#step 2:描述程式運作的條件 requirement.txt
#step 3:告訴heroku 如何執行程式 Procfile

#部署到雲端 
#利用python創造網址

from flask import Flask
app_flask = Flask(__name__)  # __name__代表目前知情的模組


@app_flask.route("/")  # decorator 函式的裝飾
def home():
    return "Hello Flask 2"


@app_flask.route("/test")  # 加在127.0.0.1:5000/後面的裝飾 #如果交給/test，給def test()處理
def test():
    return "This is Test ,very nice!"


@app_flask.route("/king")  # 127.0.0.1:5000/king
def king():
    return "Hello Laker Nation!"


if __name__ == "__main__":  # 如果以主c程式
    app_flask.run()  # 立刻啟動伺服器
