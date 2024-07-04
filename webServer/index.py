from flask import Flask
#設立了一個wedSever(伺服器)可在這邊做伺服器內容變更
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!!!</h1>"