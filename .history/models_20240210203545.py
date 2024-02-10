# from sqlalchemy import Column, Integer, String
# from database import Base

# class Items(Base):
#     __tablename__ = "items"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name= Column(String, unique=True, index=True)
#     category = Column(String)  
#     description = Column(String)
    
from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description:  str
    