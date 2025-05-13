import requests
from bs4 import BeautifulSoup
from serpapi import GoogleSearch
import os
from dotenv import load_dotenv

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

HEADERS = {"User-Agent": "Mozilla/5.0"}

def find_techcrunch_articles(company_name):
    """
    Uses SerpAPI to find top TechCrunch articles about the company.
    """
    params = {
        "engine": "google",
        "q": f"{company_name} site:techcrunch.com",
        "api_key": SERPAPI_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    articles = []
    for result in results.get("organic_results", []):
        if "techcrunch.com" in result.get("link", ""):
            articles.append({
                "title": result.get("title"),
                "url": result.get("link"),
                "snippet": result.get("snippet")
            })

    return articles[:2]  # Limit to top 2 results


def scrape_techcrunch_article(url):
    """
    Extracts relevant info from TechCrunch articles.
    """
    try:
        response = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1").get_text(strip=True)
        date = soup.find("time").get("datetime") if soup.find("time") else "No date found"
        article_body = soup.find("div", {"class": "article-content"})
        paragraphs = article_body.find_all("p") if article_body else []
        text = "\n".join(p.get_text(strip=True) for p in paragraphs)

        return {
            "url": url,
            "title": title,
            "date": date,
            "text": text[:2000]  # Truncate to keep size reasonable
        }

    except Exception as e:
        print(f"[TechCrunch ERROR]: {e}")
        return {}