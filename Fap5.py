#deep dive in pydantic from basic to advance everything.

from pydantic import BaseModel , Field

from fastapi import FastAPI

class User(BaseModel):
    user_id:int
    name:str
    age:int

app=FastAPI()

@app.get("/user/")
async def read(user:User):
    return{
        "Info":user
    }

class Address(BaseModel):
    Area:str
    house_no:int

class shop(BaseModel):
    shop_id:int = Field(gt=0 , it=100)
    shop_name:str= Field(Min_length=3 , Max_length=20)
    owner: str
    address:Address

class product(BaseModel):
    price:float=Field(gt=0)
    

