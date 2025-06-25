from fastapi import FastAPI, Request
from app.pdf_parser import parse_and_chunk
from app.ner_topic import enrich_chunks
from app.vector_store import store_enriched_chunks
from app.rag_pipeline import load_db, answer_query,similarity_search
import os


from contextlib import asynccontextmanager
from typing import AsyncIterator
import uvicorn
from pydantic import BaseModel
 
chunks = parse_and_chunk("/app/Insurance_Handbook_20103.pdf")
e_chunks = enrich_chunks(chunks)
store_enriched_chunks(e_chunks)
indices, texts, metadata = load_db()
app = FastAPI()

class chatbot(BaseModel):
    query : str

@app.post("/chat")
async def chat(request: chatbot):
    query = request.query.strip()
    if not query:
        return {"error": "Empty query"}
    
    answer = answer_query(query, indices, texts, metadata)
    return {"answer": answer}

    
















