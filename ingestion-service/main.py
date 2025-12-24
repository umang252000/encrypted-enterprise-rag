from fastapi import FastAPI, Request, Depends
from chunker import chunk_text
from embedder import generate_embedding
from encrypt import encrypt_vector, encrypt_metadata

app = FastAPI(title="Encrypted Ingestion Service")

@app.post("/ingest")
def ingest_document(request: Request, payload: dict):
    tenant = request.headers.get("X-Tenant-ID")
    text = payload.get("text")

    chunks = chunk_text(text)
    encrypted_chunks = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)
        encrypted_chunks.append({
            "vector": encrypt_vector(embedding, tenant),
            "metadata": encrypt_metadata(chunk, tenant)
        })

    return {
        "tenant": tenant,
        "chunks_ingested": len(encrypted_chunks),
        "status": "encrypted_and_stored"
    }

@app.get("/health")
def health():
    return {"status": "ingestion-ok"}