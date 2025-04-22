# 📰 News Scraper Web Application

This is a **3-tier web application** built using **FastAPI**, **MongoDB**, and a static HTML/JS frontend. It scrapes news articles from Bing News based on user input, stores the results in MongoDB, and serves them through a web interface.

---

## 🌐 Application Workflow

1. **User searches** for a news topic on the web UI.
2. The frontend sends a `GET` request to the FastAPI backend: `/search?topic=...`
3. The backend:
   - First checks MongoDB for a cached result.
   - If found, it returns cached data (`source: cache`).
   - If not found, it scrapes Bing News, stores the result in MongoDB, and returns it (`source: scraped`).
4. The UI displays the results dynamically.
5. Users can also click "Show History" to see previously searched topics.

---

## 📁 Project Structure

```
news-scraper-app/
│
├── backend/                 # FastAPI backend application
│   ├── main.py              # FastAPI endpoints and MongoDB logic
│   ├── scraper.py           # Bing News scraping logic using BeautifulSoup
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Docker image for FastAPI backend
│
├── frontend/                # Static frontend files
│   ├── index.html           # Main HTML file with input + results
│   ├── app.js               # JavaScript to call backend and update UI
│   ├── style.css            # Basic styling
│   └── favicon.ico          # Optional: tab icon
│
├── docker-compose.yml       # Docker Compose setup for 3 services
└── README.md                # Project documentation (this file)
```

---

## 🐳 Dockerized Setup

The app is composed of 3 containers:
- **backend**: FastAPI server (`localhost:8000`)
- **frontend**: Static HTML/JS served via NGINX (`localhost:8080`)
- **mongo**: MongoDB server for storing search results (`localhost:27017`)

### ▶️ Start the App

```bash
docker-compose up --build
```

### 🛑 Stop the App

```bash
docker-compose down
```

---

## 🔍 API Endpoints (via FastAPI)

- `GET /search?topic=india`  → Scrape or return cached news for "india"
- `GET /history`             → Returns list of previously searched topics with timestamps

Try out the interactive API docs at:
**http://localhost:8000/docs**

---

## 🧠 MongoDB Schema

Collection: `news`
```json
{
  "topic": "india",
  "results": [
    { "title": "...", "link": "..." },
    ...
  ],
  "created_at": "2025-04-22T14:30:00Z"
}
```

---

## 💻 Access MongoDB

```bash
docker exec -it <mongo_container_id> mongosh
use news_app
db.news.find().pretty()
```

Or use MongoDB Compass GUI with:
```
mongodb://localhost:27017
```

---

## 🔧 To Do / Next Steps
- [ ] Add pagination for large result sets
- [ ] Add expiry (TTL index) to MongoDB documents
- [ ] Use a dedicated news API for stability (optional)
- [ ] Deploy with HTTPS and domain setup

---

## 🙌 Credits
- Backend: [FastAPI](https://fastapi.tiangolo.com/)
- Scraping: [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Frontend: HTML + JS
- Database: MongoDB
- Dev & Docker: You 😉

Feel free to modify, scale, or deploy this for your learning or demos!
