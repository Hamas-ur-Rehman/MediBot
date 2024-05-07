from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from medibot_service import MediBot

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demonstration purposes
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/ask")
def ask(input_data:dict = {
    "userid": "afaq@gmail.com",
    "question": "Hi I got a nose problem"
   }):
    try:
       response = MediBot(userid=input_data.get('userid'),question=input_data.get("question"))
       return {"response":response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
