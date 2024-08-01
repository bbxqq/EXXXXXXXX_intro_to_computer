#coding=utf-8
# 不加上就無法使用中文註解
import random
from flask import *   #引入flask所有功能
app = Flask(__name__)   #創建flask實例

@app.route("/", methods = ["GET"])   #設定"/"目錄的路由, 並將方法設定為GET觸發
def webPage():   #當有人在"/"目錄下使用GET請就觸發webPage()
    return render_template('lab10.html')   #使用render_template()函數回傳一個html檔給對方瀏覽器

@app.route("/student_data", methods = ["POST"])   #設定"/"目錄的路由, 並將方法設定為GET觸發
def result():
    student_name = request.form["student_name"]
    student_id = request.form["student_id"]
    print("name:", student_name)
    print("student_id:", student_id)
    return "OK"

@app.route("/rsp", methods = ["GET"])
def rsp():
    choice = request.args.get('choice',default= "r")
    result = random.choice(["r", "s", "p"])
    print("computer:", result, "user:", choice)
    if choice not in ["r", "s", "p"]:
        return "輸入有誤，請重新出拳"
    elif result == choice:
        return "平手"
    elif (choice == "r" and result == "s") or (choice == "s" and result == "p") or (choice == "p" and result == "r"):
        return "你贏了"
    else:
        return "你輸了"

app.run(host="0.0.0.0", port=3000, debug=True)   #host設定"0.0.0.0"允許所有ip訪問, 不只限制內網