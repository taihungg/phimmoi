import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    username='root',
    password=''
)
cur = db.cursor()

cur.execute("Create Database IF NOT EXISTS phimmoi")

# print(db)




