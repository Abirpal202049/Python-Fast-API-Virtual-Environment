from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fakedb = []

class Course(BaseModel):
    id : int
    name : str
    price : float
    is_early_bird : bool

@app.get("/")
def home_route():
    return {"Hello" : "World"}


@app.get("/courses")
def get_all_course():
    return fakedb

@app.get("/course/{courseid}")
def get_course(courseid : int):
    return fakedb[courseid - 1]

@app.post("/create")
def add_post(course : Course):
    fakedb.append(course.dict())
    return {
            "message" : "Item Created Successfully", 
            "data" : fakedb[-1]
        }


@app.delete("/course/{course_id}", description="Delete a particular course with it's course id")
def delete_course(course_id: int):
    fakedb.pop(course_id - 1)
    return {
        "message" : "Item Deleted Successfully",
        "course_id" : course_id,
    }