import os
import json
import numpy as np
import faiss
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

EMBEDDING_MODEL = 'models/embedding-001'

def get_embeddings(texts: list[str]) -> np.ndarray:
    """Batch process embeddings"""
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=texts,
        task_type="retrieval_document"
    )
    return np.array(response['embedding'], dtype='float32')

def store_enriched_chunks(enriched_chunks: list[dict]):
    """Store chunks with FAISS index and metadata"""
    os.makedirs("faiss_index", exist_ok=True)
    
    texts = [e['text'] for e in enriched_chunks]
    metadata = [{'entities': e['entities'], 'topic': e['topic']} for e in enriched_chunks]
    
    # Batch process embeddings
    embeddings = get_embeddings(texts)
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    
    # Save all components
    faiss.write_index(index, "faiss_index/index.faiss")
    with open("faiss_index/metadata.json", "w") as f:
        json.dump(metadata, f)
    with open("faiss_index/texts.json", "w") as f:
        json.dump(texts, f)
    
    return index