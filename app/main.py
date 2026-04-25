from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI()

# ✅ include router (NO extra prefix)
app.include_router(auth_router)

# optional root
@app.get("/")
def root():
    return {"message": "API running"}
