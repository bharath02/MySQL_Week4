import mysql.connector
import pandas as pd
import pymysql
file=open("SalesJan2009.csv","r")
fileString=file.read()
fileList=[]
for line in fileString.split('\n'):
    fileList.append(line.split(','))

# open connection

database=pymysql.connect("localhost",'root','password','CSVFile')
cursor=database.cursor()

cursor.execute("DROP TABLE IF EXISTS Sales")

"""mycsv=mysql.connector.connect(host='localhost',user='root',password='password',database='CSVFile')
mycsvtable=mycsv.cursor()

"""
#Step 1:  Create Attributes and Variable of a Datatype
 
#CreateTable="Create table Sales(Transaction_date DATETIME, Product char(50), Price int(10),Payment_Type varchar(50), Name varchar(50),City varchar(50),State varchar(50), Country varchar(50), Account_Created varchar(50), Last_Login DATETIME, Latitude float(50),Longitude float(50))"
#mycsvtable.execute(CreateTable)
"""
# Altered: mycsvtable.execute("Alter Table Sales add Payment_Type varchar(50) After Price")

# Step 2: Insert a values of a database

insertValues= "Insert into Sales(Transaction_date, Product, Price, Payment_Type, Name, City, State, Country, Account_Created, Last_Login, Latitude, Longitude) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
values=pd.read_csv("/home/bridgelabz/Desktop/mysqlPythonWeek4/4.0_importData/SalesJan2009.csv", header=1)
mycsvtable.execute(insertValues,values)
mycsv.commit()
print(mycsvtable.rowcount, "rows inserted Sucessfully ")"""