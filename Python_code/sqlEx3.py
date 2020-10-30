import sqlite3

conn = sqlite3.connect("../DB_code/chadwick.db")

print( "Opened database successfully")

cursor = conn.execute("select yearID from Salaries limit 10")

for row in cursor:
    print("yearID=", row[0])
