import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='password',database='DB1')

mybase=mydb.cursor()

import pandas as pd
data=pd.read_sql("select * from AllDataTypes",mydb)
print(data)
data1=pd.read_sql("select * from employee",mydb)
print(data1)
data1.to_csv("/home/bridgelabz/Desktop/mysqlPythonWeek4/WorkDataTypesandKeys/Data1.csv",sep=',')