import requests
from bs4 import BeautifulSoup

def scrape_news(topic):
    url = f"https://www.bing.com/news/search?q={topic.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")

    articles = []
    for item in soup.select("a.title")[:10]:  # simple selector
        title = item.get_text(strip=True)
        link = item.get("href")
        if title and link:
            articles.append({
                "title": title,
                "link": link
            })

    return articles
