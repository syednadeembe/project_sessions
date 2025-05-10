# Stock Market App

A simple Flask-based web application to fetch and display stock market information using the Yahoo Finance API.

## Features

- Input a stock ticker and select a country (India or US) to fetch stock details.
- Displays stock information such as:
  - Stock name
  - Symbol
  - Current price
  - Previous close price
  - Market capitalization
  - Currency
- Handles errors gracefully if the stock information cannot be fetched.


## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

    Clone the repository:
   ```bash
   git clone <repository-url>
   cd stock-market-app
   pip install -r requirements.txt
   python app.py
   Open your browser and navigate to : http://127.0.0.1:5000/
   Enter a stock ticker and select a country to fetch stock information.

Example
Input: Ticker: AAPL, Country: US
Output:
Stock Name: Apple Inc.
Symbol: AAPL
Current Price: $150.00
Previous Close: $148.50
Market Cap: $2.5T
Currency: USD

## Exercise 
1. Create Docker Setup for this application 
2. Create k8s Deployment yamls and run this via ingress 
