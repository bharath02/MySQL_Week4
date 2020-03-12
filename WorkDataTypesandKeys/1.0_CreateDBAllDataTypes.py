import mysql.connector

mydatabase=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')
mytable=mydatabase.cursor()
mytable.execute("SHOW TABLES ")
for val in mytable:
    print(val)