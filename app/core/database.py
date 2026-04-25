from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# ✅ FIXED DATABASE NAME (IMPORTANT)
db = client["pis"]

users_collection = db["users"]
