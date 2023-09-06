import sqlite3
import json

f=open('C:\\Users\\Ravi\\Documents\\GitHub\\Dart\\Fluttter\\Chapter 5\\Login App\\login_app\\lib\\ui\\data.json','r', encoding='utf-8')
data=json.load(f)

# Connect to the database (a new file will be created if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table to store the JSON data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mytable1 (
        end_year TEXT,
intensity INTEGER,
sector TEXT,
topic TEXT,
insight TEXT,
url TEXT,
region TEXT,
start_year TEXT,
impact TEXT,
added TEXT,
published TEXT,
country TEXT,
relevance INTEGER,
pestle TEXT,
source TEXT,
title TEXT,
likelihood INTEGER
    )
''')
table_name = 'mytable1'  # Replace 'users' with the name of your table

# Execute a query to retrieve the table schema
cursor.execute(f"PRAGMA table_info({table_name});")

# Fetch the results
columns = cursor.fetchall()

# Display the column names and details
for column in columns:
    print(column[1])  

# Commit the changes to the database
conn.commit()
# for i in data:
#     for j in i:
#         print(j,"TEXT")
    
for item in data:
    
    cursor.execute('''
        INSERT INTO mytable1 (end_year,intensity,sector,topic,insight,url,region,start_year,impact,added,published,country,relevance,pestle,source,title,likelihood)
        VALUES (?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?)
    ''', (item['end_year'],item['intensity'],item['sector'],item['topic'],item['insight'],item['url'],item['region'],item['start_year'],item['impact'],item['added'],item['published'],item['country'],item['relevance'],item['pestle'],item['source'],item['title'],item['likelihood']))

# Commit the changes to the database

cursor.execute('SELECT * FROM mytable1')  # Replace 'mytable' with your table name
rows = cursor.fetchall()  # Fetch all rows
for row in rows:
    print(row)


conn.commit()
conn.close()
