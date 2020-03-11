import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')
mybase=mydb.cursor()
sql="UPDATE employee SET salary=22000000 WHERE firstName='Bharath'"
mybase.execute(sql)
mydb.commit()