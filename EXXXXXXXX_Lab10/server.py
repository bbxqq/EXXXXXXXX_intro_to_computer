#coding=utf-8
# 不加上就無法使用中文註解

from flask import *
app = Flask(__name__)


# 設定根目錄(通常代表首頁)之路由
# 使用render_template函式讓首頁的路由能夠回傳html檔(簡單架構)給前端，來顯示首頁畫面，而不是僅用return文字的方式
@app.route("/")
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾) 
    return render_template('app.html')


# 設定路由為/set

# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存


@app.route('/set',methods = ['POST'])
def root():
    string1 = request.form['string1']
    data = request.form.to_dict()
    print(data)
    return 'ok ! your text is : '+ string1 # 發送response為 ok + 傳送的文字內容

app.run(host="0.0.0.0", port=3000, debug=True)