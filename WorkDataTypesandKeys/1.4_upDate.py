import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')
mybase=mydb.cursor()
sql="UPDATE AllDataTypes SET DateOfBirth='1994-01-26' WHERE Id=22"
mybase.execute(sql)
mydb.commit()
print("UpDated")