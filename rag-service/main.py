from fastapi import FastAPI
from secure_prompt import build_secure_prompt
from llm_mock import run_llm
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Encrypted RAG Orchestrator")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://scaling-fortnight-jjppvpjpvg9vfgr9-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
def query_rag(payload: dict):
    tenant = payload["tenant"]
    user_query = payload["query"]
    encrypted_results = payload["encrypted_results"]

    prompt = build_secure_prompt(
        encrypted_contexts=encrypted_results,
        user_query=user_query
    )

    answer = run_llm(prompt)

    return {
        "tenant": tenant,
        "answer": answer,
        "leakage": "none"
    }

@app.get("/health")
def health():
    return {"status": "rag-ok"}