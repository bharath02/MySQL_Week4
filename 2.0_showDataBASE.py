import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='password')
mybase=mydb.cursor()
mybase.execute("Show databases")
for bata in mybase:
    print(bata)