from fastapi import FastAPI

app=FastAPI(title="My First Api" ,  version="1.0.0")

@app.get("/")
async def root():
    return {"message":"Api are Working Successfully"}

@app.get("/user_id/ {user_id}")
async def create_user(user_id:int , name:str=None):
    return{"User_is":user_id , "Name":name}

@app.post("/item/")
async def create_item(item:dict):
    return{"Item":item}



