from cryptography.fernet import Fernet

# ⚠️ Prototype keys (one per tenant)
TENANT_KEYS = {
    "tenant-a": Fernet.generate_key(),
    "tenant-b": Fernet.generate_key()
}

def encrypt_vector(vector: list, tenant_id: str):
    fernet = Fernet(TENANT_KEYS[tenant_id])
    payload = ",".join(map(str, vector)).encode()
    return fernet.encrypt(payload)

def encrypt_metadata(text: str, tenant_id: str):
    fernet = Fernet(TENANT_KEYS[tenant_id])
    return fernet.encrypt(text.encode())