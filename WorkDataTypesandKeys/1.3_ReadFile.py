import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')

mybase=mydb.cursor()
mybase.execute("select * from AllDataTypes")
myresult=mybase.fetchall()
for row in myresult:
    print(row)