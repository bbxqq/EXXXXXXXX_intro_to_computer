#coding=utf-8
# 不加上就無法使用中文註解
import random
from flask import *   #引入flask所有功能
app = Flask(__name__)   #創建flask實例

dict1 = {}

@app.route("/", methods = ["GET"])   #設定"/"目錄的路由, 並將方法設定為GET觸發
def webPage():   #當有人在"/"目錄下使用GET請就觸發webPage()
    return render_template('lab10_plus.html')   #使用render_template()函數回傳一個html檔給對方瀏覽器

@app.route("/set", methods = ["POST"])   #設定"/"目錄的路由, 並將方法設定為GET觸發
def result():
    store_name = request.form["store_name"]
    score = request.form["score"]
    dict1.setdefault(store_name, score)
    data1 = json.dumps(dict1, ensure_ascii=False)
    print(dict1)
    return render_template("lab10_plus.html", data=data1)

@app.route("/reset/<yon>", methods = ["GET"])
def reset(yon):
    print(type(yon))
    if yon == "y":
        dict1.clear()
        return render_template("reset.html")
    elif yon == "n":
        return render_template("lab10_plus.html")

app.run(host="0.0.0.0", port=3000, debug=True)   #host設定"0.0.0.0"允許所有ip訪問, 不只限制內網