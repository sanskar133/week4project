import faiss
import numpy as np
import json
from dotenv import load_dotenv
import google.generativeai as genai
from vector_store import get_embeddings
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def load_db():
    """Load existing FAISS index and metadata"""
    index = faiss.read_index("faiss_index/index.faiss")
    with open("faiss_index/metadata.json", "r") as f:
        metadata = json.load(f)
    with open("faiss_index/texts.json", "r") as f:
        texts = json.load(f)
    return index, texts, metadata

def similarity_search(query: str, index, texts: list, metadata: list, k: int = 3):
    """Search for similar documents"""
    query_vec = get_embeddings([query]).reshape(1, -1)
    distances, indices = index.search(query_vec, k)
    return [{'text': texts[i], 'metadata': metadata[i]} for i in indices[0]]

def answer_query(query: str, index, texts: list, metadata: list):
    """Generate answer using retrieved context"""
    docs = similarity_search(query, index, texts, metadata)
    context = "\n".join(doc["text"] for doc in docs)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"Answer based on this context:\n{context}\n\nQuestion: {query}"
    )
    return response.text