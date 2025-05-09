# E-Commerce App

This is a simple e-commerce application built with a **FastAPI** backend and a **React** frontend. The application uses **MongoDB** as its database.

## Project Structure

## Features

- **Backend**:
  - Built with FastAPI.
  - Provides RESTful APIs for managing products.
  - MongoDB integration for data storage.
- **Frontend**:
  - Built with React and Vite.
  - Displays product data fetched from the backend.
- **Database**:
  - MongoDB with an initialization script to seed sample data.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd ecommerce-app

2. Start the application using Docker Compose:
docker-compose up --build

3. Access the application:

Frontend: http://localhost:3000
Backend API: http://localhost:8000
MongoDB: Runs on localhost:27017 (accessible only within the Docker network).

API Endpoints
Base URL: /api/products
GET /: List all products.
POST /: Add a new product.
MongoDB Initialization
The mongo-init/init.js script initializes the MongoDB database with sample product data.

Technologies Used
Backend: FastAPI, Python, PyMongo
Frontend: React, Vite
Database: MongoDB
Containerization: Docker, Docker Compose