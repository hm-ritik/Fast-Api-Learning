#path operations 
#->path parameters
#->query parameters

from fastapi import FastAPI , HTTPException

app=FastAPI(title='path parameters' , version="7.0.0")
"""✔️ Get user by ID
   ✔️ Delete product
   ✔️ Update order"""

user={}
@app.post("/user/{user_id}/product_id/{product_id}")
async def setinfo(user_id:int , product_id:int):
    user[user_id]={
        "User id": user_id,

    }
    user[product_id]={
        "Product id": product_id
    }
    return{
       "Message": "Data Is Posted",
       "Information" : user
    }
@app.delete("/user/{user_id}/product_id/{product_id}")
async def remove(user_id:int , product_id:int):
    if user_id not in user:
        raise HTTPException(status_code=404 , detail="user id not found")
    if product_id not in user:
        raise HTTPException(status_code=404 , detail="product id not found")
    
    del user[user_id]
    del user[product_id]
    
    return{
        "Item deleted":user
    }



#FAKE DATABASE
"""user={}

# Create -> Update -> Delete -> Read

@app.post("/user/{user_id}")
async def create(user_id:int):
    user[user_id]={
        "Data": f"User created {user_id}",
        "Update": False ,
        "Delete": False
    }
    return {"Message": "user created" , "user": user[user_id]}

@app.put("/user/{user_id}")
async def update(user_id:int):
    if user_id  not in user or user[user_id]["Delete"]:
        raise HTTPException (status_code=404 , detail="user not found")
    
    user[user_id]["Update"]=True
    return {"message": "User updated", "User": user[user_id]}

@app.delete("/user/{user_id}")
async def remove(user_id:int):
    if user_id not in user:
        raise HTTPException (status_code=404 , detail="user not found")
    
    user[user_id]["Delete"]=True

    return {"Message": "User Deleted" , "User": user[user_id]}

@app.get("/user/{user_id}")
async def read(user_id:int):
    if user_id not in user:
        raise HTTPException (status_code=404 , detail="no user found")
    
    if user[user_id]["Delete"]:
        return {"Message": "User already deleted"}
    
    if user[user_id]["Update"]:
        return {"message": "user exists and updated"}
    
    return {"message": "The user is " , "User": user[user_id]} """





