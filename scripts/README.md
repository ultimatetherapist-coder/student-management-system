# Student Management System

A simple Student Management API built using Python, FastAPI, SQLite, and SQLAlchemy.

This project allows users to manage student records using CRUD operations.

## Features

- Add a new student
- View all students
- Search for a student by ID
- Update student details
- Delete a student
- Store student data in an SQLite database

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Project Structure

```text
python-for-ai/
├── main.py
├── students_db.py
├── sqlalchemy_setup.py
├── database_test.py
├── scripts/
│   ├── check_duplicates.py
│   └── remove_duplicates.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd python-for-ai
```

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the environment on Windows**

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Install the required packages**

```bash
pip install -r requirements.txt
```

**5. Start the server**

```bash
python -m uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs to test the API.

## What I Learned

- Building APIs using FastAPI
- Performing CRUD operations
- Connecting Python with SQLite
- Using SQLAlchemy to work with databases

## Author

Soham Deshmukh
