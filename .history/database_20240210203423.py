# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///./myDB.db"
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False } )
# SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from pymongo import MongoClient

client = MongoClient("mongodb+srv://ibousakhria:imed123!@cluster0.jpliqa5.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["todo"]