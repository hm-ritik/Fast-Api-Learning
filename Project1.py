#crud operation 
from fastapi import FastAPI , HTTPException 

Library={}

app=FastAPI(title="Library Api" , version="7.0.0")

@app.post("/Bookid/{book_id}")
async def create_book(book_id:int , author:str ,book_name:str):
    Library[book_id]={
        "Author":author,
        "Book Name":book_name
    }
    return{
        "Message":"Book Posted",
        "Book Id": book_id ,
        "Author" : author ,
        "Book name": book_name
    }

@app.get("/bookinfo/")
async def ficle(book_id:int):
    if book_id not in Library:
        raise HTTPException(status_code=404 , detail="Not found")
    return{
        "message": "The book is in the Database",
        "Book Info": Library[book_id]
    }

@app.put("/updatebook/{book_id}")
async def update(book_id:int, author:str, book_name:str):
    if book_id not in Library:
        raise HTTPException(status_code=404 , detail="Book Is not found in library")
    Library[book_id]["Author"] = author
    Library[book_id]["Book Name"] = book_name

    return {
        "message": "Book updated successfully",
        "data": Library[book_id]
    }


@app.get("/bookinfoo/")
async def ficlee(book_id:int):
    if book_id not in Library:
        raise HTTPException(status_code=404 , detail="Not found")
    return{
        "message": "The book is in the Database",
        "Book Info": Library[book_id]
    }

@app.delete("/book/{book_id}")
async def remove(book_id:int):
    if book_id not in Library:
        raise HTTPException(status_code=404 , detail="Book is not in Library")
    del Library[book_id]
    return{
        "Message": "The Book is successfully Removed from the Library",
        
    }

    

