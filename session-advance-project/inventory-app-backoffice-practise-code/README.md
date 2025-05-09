# 🧾 Inventory Management Web Application

A simple and modern inventory management system built for e-commerce backend teams to manage products with ease. It allows backend admins to add, view, and mark products as sold. The UI is minimalistic yet functional, and the stack is completely Dockerized for easy deployment.

## 📦 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, FastAPI
- **Database**: MongoDB
- **Containerization**: Docker, Docker Compose
- **Web Server**: Nginx (for static files)

## 🚀 Features

- Add new products with:
  - Product Name
  - Product Price
  - Product Quantity
  - Product Category
- View all added products
- Mark products as sold (Delete)
- Live search for products

## 🛠️ Folder Structure

```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── db.py
│   │   ├── models.py
│   │   └── routes/
│   │       └── products.py
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│   └── nginx.config
├── mongo-init/
│   └── init.js
├── docker-compose.yml
└── README.md
```

## ⚙️ How It Works

### 🧠 Backend - FastAPI
- `GET /api/products/`: Returns all products in JSON format
- `POST /api/products/`: Adds a new product to MongoDB
- `DELETE /api/products/{product_id}`: Deletes a product (used when marking it sold)

### 💻 Frontend - HTML + JS
- Makes API calls to `/api/products` for fetching and submitting data.
- Interacts with FastAPI using `fetch()` in `app.js`.

### 📡 Proxy Handling
- Nginx is used to serve static frontend files and reverse-proxy `/api` calls to FastAPI backend.

## 🐳 How to Run (Docker)

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/inventory-app.git
cd inventory-app
```

### 2. Run Docker Compose

```bash
docker compose up --build
```

- Access **Frontend**: http://localhost:3000
- Access **Backend**: http://localhost:8000 (for debugging)
- MongoDB runs in background with default credentials

## 📝 Notes

- If you see 403 errors from Nginx, ensure static files have correct permissions.
- MongoDB data persists in a named volume (`mongo-data`).
- You can extend the project to include auth, image upload, bulk import, etc.

## 🙌 Contributing

Want to improve the app? Pull requests are welcome!
