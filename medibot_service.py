from chromadb_service import retriver
from prompt import PROMPT
from openai_service import AskAI
from mongodb_service import *
import datetime
from custom_logger import *

def MediBot(userid:str,question:str):
    log.info("Adding Chats into MongoDB -- User")
    insert_chat(
        userid=userid,
        role="user",
        msg=question,
        created_at=datetime.datetime.now()
    )
    log.info("Retriving Data From Database")
    docs = retriver(question)
    DOC_PROMPT = 'This is from where you can possibly get information about the user question'
    for doc in docs:
        DOC_PROMPT += "\n" + doc
    messages = [
        {
            "role": "system",
            "content": PROMPT
        },
        {
            "role": "system",
            "content": DOC_PROMPT
        },
    ]

    try:
       log.info("Fetching Chats from MongoDB")
       chats = fetch_chats(userid)
       for chat in chats:
            messages.append(
            {
                "role":chat['role'],
                "content":chat["msg"]
            }
            )
    except Exception as e:
        pass
    
    messages.append({"role":"user","content":question})

    response = AskAI(messages)
    log.info("Adding Chats into MongoDB -- AI")
    insert_chat(
        userid=userid,
        role="assistant",
        msg=response,
        created_at=datetime.datetime.now()
    )
    return response

    