from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
import os

DB_PATH = "data/vector_db"

def load_vectorstore():
    embeddings = OllamaEmbeddings(model="llama3.2:3b")

    if os.path.exists(DB_PATH):
        return FAISS.load_local(DB_PATH, embeddings)

    raise Exception("Vector DB not found. Run ingest.py first.")