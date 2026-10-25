
import sqlite3

connection = sqlite3.connect("../Students.db")
cursor = connection.cursor()

cursor.execute("""
    DELETE FROM Students
    WHERE id NOT IN (
        SELECT MIN(id)
        FROM Students
        GROUP BY Name, Age, Year, Branch
    )
""")

connection.commit()

print("Duplicate records removed:", cursor.rowcount)

connection.close()
