
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import select

from sqlalchemy_setup import engine, Student as StudentModel

app = FastAPI()


# Pydantic model for creating a student
class StudentCreate(BaseModel):
    name: str
    age: int
    year: str
    branch: str


# Pydantic model for updating a student
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None
    branch: Optional[str] = None


# Helper function to format a database student as a response
def student_response(student):
    return {
        "id": student.id,
        "name": student.Name,
        "age": student.Age,
        "year": student.Year,
        "branch": student.Branch
    }


@app.get("/")
def index():
    return {"Hello": "World"}


# READ: Get student by ID
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Student ID")):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student_response(student)


# READ: Search student by name
@app.get("/get-by-name")
def get_student_by_name(name: Optional[str] = None):
    if name is None:
        raise HTTPException(
            status_code=400,
            detail="Please provide a student name"
        )

    with Session(engine) as session:
        statement = select(StudentModel).where(
            StudentModel.Name == name
        )
        student = session.scalars(statement).first()

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student_response(student)


# CREATE: Add a student
@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: StudentCreate):
    with Session(engine) as session:
        existing_student = session.get(StudentModel, student_id)

        if existing_student is not None:
            raise HTTPException(
                status_code=409,
                detail="Student already exists"
            )

        new_student = StudentModel(
            id=student_id,
            Name=student.name,
            Age=student.age,
            Year=student.year,
            Branch=student.branch
        )

        session.add(new_student)
        session.commit()
        session.refresh(new_student)

        return student_response(new_student)


# UPDATE: Update an existing student
@app.put("/update_student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    with Session(engine) as session:
        existing_student = session.get(StudentModel, student_id)

        if existing_student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        updates = student.model_dump(
            exclude_unset=True,
            exclude_none=True
        )

        field_mapping = {
            "name": "Name",
            "age": "Age",
            "year": "Year",
            "branch": "Branch"
        }

        for field, value in updates.items():
            setattr(existing_student, field_mapping[field], value)

        session.commit()
        session.refresh(existing_student)

        return student_response(existing_student)


# DELETE: Delete a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    with Session(engine) as session:
        student = session.get(StudentModel, student_id)

        if student is None:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        session.delete(student)
        session.commit()

        return {"Message": "Student deleted successfully"}
