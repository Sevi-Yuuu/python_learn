import pymysql

db = pymysql.connect(
    host="172.18.178.136",
    port=6716,
    user='****',
    password="******",
    database="db01",
    charset='utf8mb4'
)
