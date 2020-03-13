from pymongo import MongoClient

from pprint import pprint
client =MongoClient()
database=client.test
"""data={'ID':1,
      'Name':"Bharath",
      'Phone':9603104321,
      'age':26,
      'Address':'Hyderabad',
      'PinCode':505184}
database.Details.insert(data)"""
#database.Details.update({'Address':'Hyderabad'},{'Address':'Manthani'})
"""database.Details.remove({'Address':'Manthani'})
for data in database.Details.find():
    print(data)"""
data=database.Product
'''ProductDetail={'ProductName':input("Enter a Name : "),
               'CostProduct':input("Enter a {} cost : ".format('ProductName')),
               'Quantity':input("Enter Quantity {} : ".format('ProductName'))}
ResultProduct=data.insert(ProductDetail)
pprint(ResultProduct)'''

"""
# find a  value in a Data :

ResultFind=data.find_one({'Quantity':input('Enter a Quantity value to find : ')})

pprint(ResultFind)"""
"""
# Update_one
database.Product.update_one({'Quantity':input("Enter a Quantity of a Product : ")},
                            {"$set":{'ProductName':input("Enter a Name : "),
                                     'CostProduct':input("Enter a {} cost : ".format('ProductName')),
                                     'Quantity':input("Enter Quantity {} : ".format('ProductName'))}})
checkUPdate=database.Product.find_one({'Quantity':input("Enter a Quantity of a Product : ")})"""
#database.Product.delete_one({'Quantity':input("Enter a Quantity of a Product : ")})
for data in database.Product.find():
    print(data)