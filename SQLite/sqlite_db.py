#!/usr/bin/env python3
import sqlite3

connection = sqlite3.connect("chinook.db") #SQLite Sample Database
cursor = connection.cursor()

cursor.execute("Select * From albums")
result = cursor.fetchall()
for i in result:
    print(i)
connection.close()