import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='password')
mybase=mydb.cursor()
if(mydb):
    print("connection Sucessfull")
else:
    print("connection is UnsuccessFull")
mybase.execute("CREATE DATABASE DB1")


