import sqlite3

def add_student(Name, Age, Year, Branch):
    connection = sqlite3.connect("Students.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Age INTEGER NOT NULL,
            Year TEXT NOT NULL,
            Branch TEXT NOT NULL
        )
    """)

    cursor.execute("""
        INSERT INTO Students (Name, Age, Year, Branch)
        VALUES (?, ?, ?, ?)
    """, (Name, Age, Year, Branch))
    connection.commit()
    connection.close()
def get_students():
    connection = sqlite3.connect("Students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()

    connection.close()
    return students


add_student('Anand', 20, 'TY', 'CSE')
print(get_students())

def get_students_by_id(student_id):
    connection = sqlite3.connect("Students.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Students WHERE id = ?", (student_id,))

    student_id = cursor.fetchone()
    connection.close()
    return student_id 
student = get_students_by_id(1)
if student is None:
   print("Student Doesnt exists")
else:
   print(get_students_by_id(1))

def delete_student(student_id):
    connection = sqlite3.connect("Students.db")
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Students WHERE id = ?" , (student_id,))
    if cursor.rowcount == 0:
        message = "Student id doesnt exists"
    else:
        message = "Student deleted successfully"
    connection.commit()
    connection.close()
    return message
print(delete_student(6))

def update_student( student_id , Name , Age , Year , Branch):
    connection = sqlite3.connect("Students.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE Students SET  Name = ? ,Age = ? ,Year = ? , Branch =? WHERE id = ?",( Name , Age , Year , Branch , student_id),)
    if cursor.rowcount == 0:
        message = "Student Doesnt Exists"
    else:
        message = "Student Updated Successfully"
        connection.commit()
        connection.close()
    return message
print(update_student(4,'Rahul' ,29 ,'last','MBBS' ))