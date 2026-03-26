from fastapi import APIRouter
from app.services.rag_service import ask_question

router = APIRouter()

@router.post("/query")
def query(q: str):
    response = ask_question(q)
    return {"response": response}