from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auth import router as auth_router

app = FastAPI()

# ✅ CORS FIX (VERY IMPORTANT)
origins = [
    "https://clinic-client-nine.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routes
app.include_router(auth_router)

# test route
@app.get("/")
def root():
    return {"message": "API running"}
