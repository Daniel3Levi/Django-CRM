import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
)

# cursor object
cursorObject = database.cursor()

# create database

cursorObject.execute("CREATE DATABASE dcrm")
print("Database created successfully.")
