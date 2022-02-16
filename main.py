#python
from tokenize import Name
from turtle import title
from typing import Optional
from unicodedata import name

#Pydantic
from pydantic import BaseModel

#FastApi
from fastapi import FastAPI, Path
from fastapi import Body, Query, Path

app = FastAPI()

#path operations-----------------------------------------------------------
@app.get("/")
def home():
    return {"hello":"world"}

@app.get("/users")
def get_users():
    return {"id":"1"}

#path parameters------------------------------------------------------------


#req_resp_body---------------------------------------------------------------
#Models
class Person(BaseModel):
    name: str
    last_name: str
    age: Optional[str] = None #por defecto es None, y si me pasan algo espero un str

@app.post("/person/new")
def create_person(person: Person = Body(...)): #indico en body(...) que es obligatorio
    return person


#validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length= 50,
        title="Person name",
        description="This is the person name, It's between 1 and 50 characters"
        ),
    age: Optional[str] = Query(
        None,
        min_length=1,
        max_length=3,
        title = "Person Age",
        description="This is the person age, It's optional"
    )
):
    return {name:age}



#validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(..., min_length=1, max_length=10, gt=0)
):
    return {person_id: "It exists!"}