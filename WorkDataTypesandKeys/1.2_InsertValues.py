import mysql.connector

mydatabase=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')
mytable=mydatabase.cursor()
myvalue="INSERT INTO AllDataTypes (ID,firstName, lastName, age, salary, phone, Address, DateOfBirth) VALUES (%s ,%s, %s, %s, %s, %s, %s, %s)"
valu=(22,'Bharath','Kumar',26,20202200, 97000285, 'Hyderabad, Telangana, 500030','19940202')
mytable.execute(myvalue,valu)
mydatabase.commit()
print(mytable.rowcount,"Record Inserted ")