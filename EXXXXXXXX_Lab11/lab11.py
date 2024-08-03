# 臺南市公有免費停車場
# https://data.gov.tw/dataset/102775

import pymysql.cursors
import requests
import json

#GET API data
test = requests.get("https://citypark.tainan.gov.tw/App/parking.ashx?verCode=5177E3481D&type=1&ftype=1&exportTo=2")   #發送GET請求並獲取json檔
r = json.loads(test.text)   #將json轉換回字典(透過GET請求下來的json是純字串)

#Connect to the database
try:
    connection = pymysql.connect(host='localhost',  # 你伺服器/主機
                                 user='n11257080',       # 你資料庫的帳號
                                 password='0000', # 你資料庫的密碼
                                 database='wordpress',     # 你資料庫的名稱
                                 cursorclass=pymysql.cursors.DictCursor)   #將獲取資料的格式改成字典(默認是元祖)
    print("連線成功")     
except Exception as error: # 出現意外時印出
    print(error)


with connection:
    with connection.cursor() as cursor:

        # SQL語法不會考
        sql = "INSERT INTO `臺南市公有免費停車場` (`停車場型態`, `停車場名稱`, `停車場地址`, `停車場電話`) VALUES (%s, %s, %s, %s)"
        for i in r:
            # 確保所有欄位都有值，否則使用預設值
            停車場型態 = i.get('停車場型態') or '未知'
            停車場名稱 = i.get('停車場名稱') or '未知'
            停車場地址 = i.get('停車場地址') or '未知'
            停車場電話 = i.get('停車場電話')
                
            if 停車場電話 is None:
                停車場電話 = '無'

            cursor.execute(sql, (
                停車場型態,
                停車場名稱,
                停車場地址,
                停車場電話
            ))

    connection.commit()
    cursor.close()
