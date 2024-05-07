from chromadb_service import retriver
from prompt import PROMPT
from openai_service import AskAI

def MediBot():
    question = input("Enter your question: ")
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
            "role": "user",
            "content": question
        },
        {
            "role": "system",
            "content": DOC_PROMPT
        }
    ]

    response = AskAI(messages)

    print(response,"\n")

    
MediBot()