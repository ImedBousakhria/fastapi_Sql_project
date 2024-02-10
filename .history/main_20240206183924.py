from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
app = FastAPI()


models.Base.metadata.create_all(bind=engine)



def get_db():
    try:
        db = SessionLocal()            
        yield db
        
    finally:
        db.close()

    
    
    
class Item(BaseModel):
    name: str = Field(min_length=1)
    category:str = Field(min_length=1) 
    description: str = Field(min_length=1)



todos = [ { 
           "id": 1 , 
           "todo": "Imed studying"}, {
           "id": 2 , 
           "todo": "Imed playing"}, ]
@app.get("/", tags=['ROOT'])
async def root() -> dict: #return type dict
    return {"Ping": "Pong"}

@app.get("/todos", tags=['TODOS'])
async def get_todos(db: Session = Depends(get_db())) -> dict :
    return { "data": db.query(models.Items).all() }




@app.post("/todos/add_todo", tags=['TODOS'])
async def add_todo(todo: Item, db: Session = Depends(get_db())):
    todo_model = models.Items()
    todo_model.name = todo.name
    todo_model.category = todo.category
    todo_model.description = todo.description
    db.add(todo_model)    
    db.commit()
    db.refresh()
    return 'A todo has been added successfully'



@app.put("/todos/update_todo/{id}", tags=['TODOS'])
async def edit_todo(id: int, body: dict):
    for todo in todos:
        if todo['id'] == id:
            todo.update(body)
            return {'msg': f"Todo with id {id} updated."}
    
@app.delete("/todos/delete_todo/{id}", tags=['TODOS'])
async def delete_todo(id: int):
    for todo in todos:
        if todo['id'] == id:
            todos.remove(todo)
            return {'msg': f"Todo with id {id} deleted."}
    