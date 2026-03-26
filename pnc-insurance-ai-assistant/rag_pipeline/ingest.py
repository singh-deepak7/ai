import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings


DATA_PATH = "data/raw"
DB_PATH = "data/vector_db"

def ingest():
    docs = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="llama3.2:3b")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(DB_PATH)
    print("✅ Ingestion complete")

if __name__ == "__main__":
    ingest()