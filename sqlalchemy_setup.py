from sqlalchemy.orm import DeclarativeBase , Mapped , mapped_column , Session
from sqlalchemy import Integer , String , select
from sqlalchemy import create_engine

engine = create_engine("sqlite:///../Students.db")

print("Database engine created successfully!")
with engine.connect() as connection:
    print("Connected to Students.db successfully!")
class Base(DeclarativeBase):
    pass
class Student(Base):
    __tablename__ = "Students"
    id :        Mapped[int] = mapped_column(Integer , primary_key =True)
    Name:       Mapped[str] = mapped_column(String)
    Age:        Mapped[int] = mapped_column(Integer)
    Year:       Mapped[str] = mapped_column(String)
    Branch:     Mapped[str] = mapped_column(String)


def get_student_by_id(student_id):
    with Session(engine) as session:
        statement = select(Student).where(Student.id == student_id)
        student = session.scalars(statement).first()

        return student


def add_student(Name , Age , Year , Branch):
    with Session(engine) as session:
        student = Student(
            Name = Name,
            Age = Age,
            Year = Year,
            Branch = Branch
        )

        session.add(student)
        session.commit()

        return "Student Added Successfully"
# print(add_student("Test Student" , 19 , "SY" , "Electrical"))

def update_student(student_id , Name , Age , Year , Branch):
    with Session(engine) as session:
        student = session.get(Student , student_id)
        if student is None:
            return "Student Doesnt Exists"
        
        student.Name = Name
        student.Age = Age
        student.Year = Year
        student.Branch = Branch
        session.commit()
        return "Student Updates Successfully"
# print(update_student(4 ,"Test Student" , 19 , "SY" , "Electrical" ))

def delete_student(student_id):
    with Session(engine) as session:
        student = session.get(Student , student_id)
        if student is None:
            return "Student Doesnt Exists"
        session.delete(student)
        session.commit()

        return "Student Deleted Succesfully"
# print(delete_student(4))

