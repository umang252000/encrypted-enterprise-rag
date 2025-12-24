from fastapi import Request, HTTPException

def require_role(allowed_roles):
    def checker(request: Request):
        user = request.state.user
        if user["role"] not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return checker