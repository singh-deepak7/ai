from langchain_community.llms import Ollama
from rag_pipeline.vector_store import load_vectorstore

import time
from datetime import datetime

# Load once
vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

llm = Ollama(
    model="llama3.2:3b",
    num_predict=150,
    temperature=0.3
)

def format_docs(docs):
    return "\n\n".join([doc.page_content[:600] for doc in docs])

def research(sub_question: str):
    now = datetime.now().astimezone()  # local timezone
    formatted_time = now.strftime("%m-%d-%y %H:%M:%S.%f %Z")[:-3]
    print(f"Research started ... {formatted_time}")
    docs = retriever.invoke(sub_question)
    context = format_docs(docs)

    prompt = f"""
    Answer briefly based only on context.

    Context:
    {context}

    Question:
    {sub_question}

    Answer:
    """

    return llm.invoke(prompt)