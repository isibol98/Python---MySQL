#!/usr/bin/env python3
from connection import p_db
from mysql.connector import Error

mycursor = p_db.cursor() 
sql = "Select p.name,p.price,c.name From Products as p inner join Categories as c on c.id=p.categoryId where p.name='iPhone'" # ??
mycursor.execute(sql) 
        
""" for product in result:
    print(f"Product Name: {product[1]}, Price: {product[2]}, Category: {product[3]}")
    """
try:
    result = mycursor.fetchall()
    for product in result: 
        print(product)
except Error as err:
    print("Error:", err)
finally:
    p_db.close()
    print("Database closed.")