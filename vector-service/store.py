# In-memory encrypted vector store (prototype)
# Structure:
# { tenant_id: [ { "vector": enc_blob, "metadata": enc_meta } ] }

VECTOR_DB = {}

def insert_vector(tenant_id: str, encrypted_vector: bytes, encrypted_metadata: bytes):
    if tenant_id not in VECTOR_DB:
        VECTOR_DB[tenant_id] = []

    VECTOR_DB[tenant_id].append({
        "vector": encrypted_vector,
        "metadata": encrypted_metadata
    })

def get_vectors(tenant_id: str):
    return VECTOR_DB.get(tenant_id, [])