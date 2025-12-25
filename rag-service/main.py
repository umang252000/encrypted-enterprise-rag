import os
import requests
from fastapi import FastAPI
from secure_prompt import build_secure_prompt
from llm_mock import run_llm
from fastapi.middleware.cors import CORSMiddleware

VECTOR_SERVICE_URL = os.getenv("VECTOR_SERVICE_URL")

app = FastAPI(title="Encrypted RAG Orchestrator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
def query_rag(payload: dict):
    tenant = payload["tenant"]
    user_query = payload["query"]
    encrypted_results = payload["encrypted_results"]

    vector_results = requests.post(
        f"{VECTOR_SERVICE_URL}/search",
        json={
            "tenant": tenant,
            "query_vector": "ENCRYPTED_QUERY_VECTOR",
            "top_k": 3
        },
        timeout=10
    ).json()

    prompt = build_secure_prompt(
        encrypted_contexts=encrypted_results,
        user_query=user_query
    )

    answer = run_llm(prompt)

    return {
        "tenant": tenant,
        "answer": f"Secure answer generated for: {query_text}",
        "leakage": "none"
    }

@app.get("/health")
def health():
    return {"status": "rag-ok"}
