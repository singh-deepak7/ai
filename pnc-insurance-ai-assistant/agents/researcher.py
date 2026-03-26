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
    context = []
    sources = []

    for doc in docs:
        text = doc.page_content[:500]
        context.append(text)

        meta = doc.metadata
        source = meta.get("source", "unknown")
        page = meta.get("page", "N/A")
        doc_type = meta.get("doc_type", "general")

        sources.append(f"{source} (Page {page}, Type: {doc_type})")

    return "\n\n".join(context), list(set(sources))

def research(sub_question: str):
    now = datetime.now().astimezone()  # local timezone
    formatted_time = now.strftime("%m-%d-%y %H:%M:%S.%f %Z")[:-3]
    print(f"Research started ... {formatted_time}")
    docs = retriever.invoke(sub_question)

    context, sources = format_docs(docs)

    prompt = f"""
    Answer briefly (2-4 sentences) using only the context.

    Context:
    {context}

    Question:
    {sub_question}

    Answer:
    """

    answer = llm.invoke(prompt)

    return {
        "question": sub_question,
        "answer": answer,
        "sources": sources
    }