from fastapi import APIRouter, HTTPException
from app.core.database import users_collection

# ✅ single prefix
router = APIRouter(prefix="/auth")

@router.post("/login")
def login(data: dict):
    username = data.get("username")
    password = data.get("password")

    # find user
    user = users_collection.find_one({
        "username": username
    })

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    # simple password check
    if str(password).strip() != str(user.get("password", "")).strip():
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # approval check
    if not user.get("is_approved", True):
        raise HTTPException(status_code=403, detail="Not approved")

    return {
        "access_token": "dummy_token",
        "user": username
    }
