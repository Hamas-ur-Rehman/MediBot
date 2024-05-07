import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING, DESCENDING
load_dotenv()
def insert_chat(**kwargs):
    con=os.getenv("MONGODB")
    with MongoClient(con) as client:
        client["medibot"]["chats"].insert_one(kwargs)

def fetch_chats(userid:str):
    con=os.getenv("MONGODB")
    with MongoClient(con) as client:
        cursor= client["medibot"]["chats"].find({"userid":userid}).sort("created_at",DESCENDING).limit(6)
        chats= list(cursor)
        return(chats)
    

