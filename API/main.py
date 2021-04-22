from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

fakedb = []


class Course(BaseModel):
    id: int
    name: str
    is_early_bird: Optional[bool] = None


@app.get("/")
def read_root():
    return{
        "greetings": "Welcome to te Website of Coding Paradise",
        "harish": "developer"
    }


@app.get("/courses")
def access_path():
    return fakedb


@app.get("/courses/{course_id}")
def access_path(course_id: int):
    course = course_id-1
    return fakedb[course]


@app.get("/courses/{course_id}")
def access_path(course_id: int):
    course = course_id-1
    return fakedb[course]


@app.post("/courses")
def add_course(course: Course):
    fakedb.append(course.dict())
    return fakedb[-1]


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    fakedb.pop(course_id-1)
    return {"task": "Deletion success"}
