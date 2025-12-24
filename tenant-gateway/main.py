from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.responses import JSONResponse

from auth_middleware import verify_jwt
from dependencies import require_role

app = FastAPI(title="Tenant Gateway")

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    try:
        await verify_jwt(request)
        return await call_next(request)
    except HTTPException as e:
        return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail},
        )

@app.get("/secure-info")
def secure_info(
    request: Request,
    user=Depends(require_role(["admin", "user"]))
):
    return {
        "message": "Access granted",
        "tenant": request.state.user["tenant"],
        "role": request.state.user["role"]
    }

@app.get("/health")
def health():
    return {"status": "tenant-gateway-ok"}