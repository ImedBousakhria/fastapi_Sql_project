from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

import models
from sqlalchemy.orm import Session
app = FastAPI()


class Item(BaseModel):
    id: UUID
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
async def get_todos() -> dict :
    return { "data": todos }

@app.post("/todos/add_todo", tags=['TODOS'])
async def add_todo(todo: dict):
    todos.append(todo)
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
    