from sqlalchemy import Column, Integer, String
from database import Base

class Items(Base):
    __tablename__ = "items"
    
    