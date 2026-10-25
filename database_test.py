import sqlite3
connection = sqlite3.connect("Students.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       Name TEXT NOT NULL,
       Age INTEGER NOT NULL,
       Year TEXT NOT NULL,
       Branch TEXT NOT NULL)
""")
cursor.execute("""
INSERT INTO Students (Name , Age ,Year , Branch)
VALUES(?,?,?,?)
""",( 'Soham' , 19 , 'SY' , 'Electrical'))
connection.commit()
connection.close()
print("Students table created succesfully")