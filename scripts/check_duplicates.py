import sqlite3

connection = sqlite3.connect("../Students.db")
cursor = connection.cursor()

cursor.execute("""
    SELECT Name, Age, Year, Branch, COUNT(*) AS total
    FROM Students
    GROUP BY Name, Age, Year, Branch
    HAVING COUNT(*) > 1
""")

duplicates = cursor.fetchall()

for student in duplicates:
    print(student)

connection.close()