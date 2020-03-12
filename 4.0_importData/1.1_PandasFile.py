from sqlalchemy import create_engine
import pandas as pd
data=pd.read_csv('/home/bridgelabz/Desktop/mysqlPythonWeek4/4.0_importData/SalesJan2009.csv',header=0)
print(data)
engine=create_engine('mysql://root:password@localhost/Scales')
with engine.connect() as conn, conn.begin():
    data.to_sql('csv', conn, if_exists='append', index=False)
