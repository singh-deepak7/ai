from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from rag_pipeline.vector_store import load_vectorstore

vectorstore = load_vectorstore()

llm = Ollama(model="llama3.2:3b")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever()
)

def ask_question(query: str):
    return qa_chain.run(query)