from fastapi import FastAPI, HTTPException, Depends
from models import LoginRequest
from jwt_utils import create_access_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Multi-Tenant Auth Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://scaling-fortnight-jjppvpjpvg9vfgr9-3000.app.github.dev"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ⚠️ Prototype-only users
FAKE_USERS = {
    "alice": {"password": "alice123", "tenant": "tenant-a", "role": "admin"},
    "bob": {"password": "bob123", "tenant": "tenant-b", "role": "user"}
}

@app.post("/login")
def login(request: LoginRequest):
    user = FAKE_USERS.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "sub": request.username,
        "tenant": user["tenant"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "tenant": user["tenant"],
        "role": user["role"]
    }

@app.get("/health")
def health():
    return {"status": "auth-service-ok"}