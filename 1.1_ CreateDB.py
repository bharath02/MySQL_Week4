import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='password',database='DB1')
mybase=mydb.cursor()
#mybase.execute("Create table employee(firstName varchar(50), lastName varchar(50),age int(10),salary int(20))")
mybase.execute("Show tables")
for table in mybase:
    print(table)