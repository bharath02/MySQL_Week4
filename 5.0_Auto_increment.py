import mysql.connector as mc
import sqlite3 as sql

data=mc.connect(host='localhost',user='root',password='password',database='DB1')
database=data.cursor()
#database.execute("""CREATE TABLE AutoInct(id integer PRIMARY KEY, salary integer)""")
sqlb='Insert into AutoIncrement(salary) values(?)'
val=[(9000),(8000),(5000)]
database.execute(sqlb,val)
data.commit()