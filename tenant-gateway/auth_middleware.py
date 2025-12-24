from fastapi import Request, HTTPException
from jose import jwt, JWTError

SECRET_KEY = "DEV_ONLY_SECRET_CHANGE_LATER"
ALGORITHM = "HS256"

PUBLIC_PATHS = {
    "/",
    "/health",
    "/docs",
    "/openapi.json",
    "/favicon.ico"
}

async def verify_jwt(request: Request):
    if request.url.path in PUBLIC_PATHS:
        return

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing auth token")

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        request.state.user = {
            "username": payload.get("sub"),
            "tenant": payload.get("tenant"),
            "role": payload.get("role"),
        }
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")