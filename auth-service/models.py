from pydantic import BaseModel
from typing import List

class User(BaseModel):
    username: str
    tenant_id: str
    role: str  # admin | user | auditor

class TokenData(BaseModel):
    username: str
    tenant_id: str
    role: str

class LoginRequest(BaseModel):
    username: str
    password: str