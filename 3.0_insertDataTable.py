import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root',password='password',database='DB1')
mybase=mydb.cursor()
sqlForm="Insert into employee(firstName, lastName, age, salary) values(%s,%s,%s,%s)"
rawData=[('Bharath','Kumar',26,2000000),('Harika','Bha',26,3000000),('Naresh','Goud',26,4000000),('Suvam','Parida',26,4100000),]
mybase.executemany(sqlForm,rawData)
mydb.commit()