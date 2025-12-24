from fastapi import FastAPI
from store import insert_vector, get_vectors
from encrypted_similarity import pseudo_secure_similarity
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Encrypted Vector Search Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://scaling-fortnight-jjppvpjpvg9vfgr9-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/store")
def store_vector(payload: dict):
    tenant = payload["tenant"]
    vector = payload["vector"]
    metadata = payload["metadata"]

    insert_vector(tenant, vector, metadata)
    return {"status": "encrypted_vector_stored"}

@app.post("/search")
def search(payload: dict):
    tenant = payload["tenant"]
    query_vector = payload["query_vector"]
    top_k = payload.get("top_k", 3)

    candidates = get_vectors(tenant)
    scored = []

    for item in candidates:
        score = pseudo_secure_similarity(
            query_vector.encode("utf-8"),
            item["vector"].encode("utf-8")
        )
        scored.append({
            "score": score,
            "metadata": item["metadata"]
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {"results": scored[:top_k]}

@app.get("/health")
def health():
    return {"status": "vector-search-ok"}