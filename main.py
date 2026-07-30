from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Juan Bros", "grade": "A", "image": "https://example.com/images/luwi.jpg"},
    {"id": 2, "name": "Audria Syria", "grade": "B", "image": "https://example.com/images/audria.jpg"}
]

@app.get("/")
def home():
    return {"message": "Welcome to Student Info API"}

@app.get("/students")
def get_students():
    return {"students": students}
