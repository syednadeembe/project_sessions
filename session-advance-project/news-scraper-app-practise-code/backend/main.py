from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from datetime import datetime
from scraper import scrape_news
import os

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")
client = MongoClient(MONGO_URL)
db = client["news_app"]
collection = db["news"]

@app.get("/search")
async def search_news(topic: str):
    existing = collection.find_one({"topic": topic})
    if existing:
        return {"source": "cache", "results": existing["results"]}

    results = scrape_news(topic)
    collection.insert_one({"topic": topic, "results": results, "created_at": datetime.utcnow()})
    return {"source": "scraped", "results": results}

@app.get("/history")
async def get_history():
    history = collection.find({}, {"_id": 0, "topic": 1, "created_at": 1})
    return list(history)
