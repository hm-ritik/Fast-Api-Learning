#this section is about pydantic module , which is use for data validation and data prasing
# Basic Pydantic Concepts 

from pydantic import BaseModel
from fastapi import FastAPI

user={}

app=FastAPI()

class User(BaseModel):
    id:int
    name:str
    age:int

@app.post("/User")
async def create(user:User):
    return{
        "data":"The Provided Data",
        "USER": user
    }  

@app.get("/user/")
async def read(id:int , name:str , age:int):
    return{
        "Data provided":{
            "id": id,
            "name": name,
            "age": age
        }
    }