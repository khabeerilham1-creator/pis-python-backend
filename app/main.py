from fastapi import FastAPI
from app.routes.auth import router as auth_router

app = FastAPI()

# ✅ IMPORTANT: NO prefix here
app.include_router(auth_router)

# optional root (so / doesn't show 404)
@app.get("/")
def root():
    return {"message": "API running"}
