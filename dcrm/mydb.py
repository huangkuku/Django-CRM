import mysql.connector

# 建立db connector物件
dataBase = mysql.connector.connect(
    host ='localhost',
    port = '3306',
    user = 'root',
    password = 'fj03664'
)

# cursor object
cursorObject = dataBase.cursor()

# create a Datebase: cursorObject.execute(SQL Commend), SQL Commend: "sql 指令"
cursorObject.execute("CREATE DATABASE elderco")

print('All Done !')
