import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='password',database='DB1')
mybase=mydb.cursor()
sql="DELETE From employee WHERE lastName='Goud'"
mybase.execute(sql)
mydb.commit()