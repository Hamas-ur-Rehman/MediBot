import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import shutil
load_dotenv()

def loader():
    embeddings = OpenAIEmbeddings()
    if os.path.exists("./chromadb"):
        shutil.rmtree("./chromadb")
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="diseases"
        )
    root_path = './dataset'
    DATASET = []
    items = os.listdir(root_path)
    for i in items:
        with open(f"{root_path}/{i}",'r') as f:
            DATASET.append(f.read())
    
    Chroma.add_texts(vectorstore, DATASET)
    

def retriver(question:str):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="diseases"
        )
    DOCS = []
    for i in vectorstore.similarity_search(question, k=4):
        DOCS.append(i.page_content)
    return DOCS
