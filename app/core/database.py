from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

# ✅ IMPORTANT: correct DB name
db = client["pis"]

users_collection = db["users"]
