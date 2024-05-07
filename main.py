from chromadb_service import retriver

def MediBot():
    question = input("Enter your question: ")
    docs = retriver(question)
    PROMPT=f"""
     You  

    """



MediBot()