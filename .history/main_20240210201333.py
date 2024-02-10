from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://ibousakhria:<password>@cluster0.jpliqa5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)