from fastapi import FastAPI
from typing import List

app = FastAPI()

students = [
    {"id": 1, "name": "Juan Bros", "grade": "A", "image": "https://example.com/images/luwi.jpg"},
    {"id": 2, "name": "Audria Syria", "grade": "B", "image": "https://example.com/images/audria.jpg"}
]

@app.get("/")
def home():
    return {"message": "Welcome to Student Info API"}

@app.get("/students", response_model=List[dict])
def get_students():
    return students
