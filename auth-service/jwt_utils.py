from datetime import datetime, timedelta
from jose import jwt, JWTError
from models import TokenData

SECRET_KEY = "DEV_ONLY_SECRET_CHANGE_LATER"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenData(
            username=payload["sub"],
            tenant_id=payload["tenant"],
            role=payload["role"]
        )
    except JWTError:
        raise Exception("Invalid or expired token")