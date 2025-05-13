import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_crunchbase_data(crunchbase_url: str) -> dict:
    """
    Scrapes Crunchbase for funding and investor info from a public org page.
    Assumes full URL (https://www.crunchbase.com/organization/posthog)

    NOTE: This is pretty limited in functionality without their paid API.
    My hope is to get their API soon and use it to gather better insights.
    I don't use this in the final product, but wanted to include it in case you find it useful.
    """

    try:
        response = requests.get(crunchbase_url, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        data = {
            "url": crunchbase_url,
            "funding": None,
            "last_funding_type": None,
            "investors": [],
            "description": None
        }

        # Funding info usually in <span> tags
        for span in soup.find_all("span"):
            text = span.get_text(strip=True)
            if "Total Funding Amount" in text:
                next_elem = span.find_next("span")
                if next_elem:
                    data["funding"] = next_elem.get_text(strip=True)
            elif "Last Funding Type" in text:
                next_elem = span.find_next("span")
                if next_elem:
                    data["last_funding_type"] = next_elem.get_text(strip=True)
            elif "Investor Name" in text:
                investor = span.find_next("span")
                if investor:
                    data["investors"].append(investor.get_text(strip=True))

        # Try to find a description
        desc_tag = soup.find("meta", attrs={"name": "description"})
        if desc_tag:
            data["description"] = desc_tag.get("content")

        return data

    except Exception as e:
        print(f"[Crunchbase ERROR]: {e}")
        return {}
