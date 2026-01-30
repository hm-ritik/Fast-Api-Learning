from fastapi import FastAPI
# import the fastapi module 

app=FastAPI()
#create an object of fastapi

# define a root endpoint

@app.get("/")
# define a function to handle requests to the root endpoint
def root():
    return {"message": "Api created successfully"}