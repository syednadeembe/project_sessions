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
    for item in soup.select("a.title")[:10]:
        title = item.get_text(strip=True)
        link = item.get("href")
        if title and link:
            articles.append({"title": title, "link": link})
    return articles

if __name__ == "__main__":
    print(scrape_news("india"))


# import requests
# from bs4 import BeautifulSoup

# def scrape_news(topic):
#     url = f"https://www.bing.com/news/search?q={topic.replace(' ', '+')}"
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }

#     resp = requests.get(url, headers=headers)
#     soup = BeautifulSoup(resp.text, "html.parser")

#     articles = []
#     for item in soup.select(".news-card, .t_s .title")[:10]:
#         title_tag = item.select_one("a")
#         if title_tag:
#             title = title_tag.get_text(strip=True)
#             link = title_tag.get("href")
#             if title and link:
#                 articles.append({"title": title, "link": link})

#     return articles
