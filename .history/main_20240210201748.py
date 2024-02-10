from fastapi import FastAPI, Depends
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = FastAPI()

uri = "mongodb+srv://ibousakhria:imed123!@cluster0.jpliqa5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)