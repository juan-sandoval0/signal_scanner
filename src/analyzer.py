from src.web_scraper import Website
from src.prompt_engine import classify_links
from src.techcrunch_scraper import find_techcrunch_articles, scrape_techcrunch_article

def collect_all_details(company_name, url):
    """
    Scrapes main page + relevant subpages, returns a dictionary of all comapny details.
    """
    main_site = Website(url)
    filtered_links = classify_links(url, main_site.links)

    summary = {
        "company_name": company_name,
        "homepage": {
            "url": url,
            "title": main_site.title,
            "text": main_site.text
        },
        "subpages": [],
        "techcrunch_articles": []
    }

    for link in filtered_links.get("links", []):
        try:
            subpage = Website(link["url"])
            summary["subpages"].append({
                "type": link["type"],
                "url": link["url"],
                "title": subpage.title,
                "text": subpage.text
            })
        except Exception as e:
            print(f"Could not fetch {link['url']}: {e}")

   # Integrates Tech Crunch Data
    try:
        articles = find_techcrunch_articles(company_name)
        for article in articles:
            full_article = scrape_techcrunch_article(article["url"])
            if full_article:
                summary["techcrunch_articles"].append(full_article)
    except Exception as e:
        print(f"TechCrunch scraping failed: {e}")
    
    return summary
