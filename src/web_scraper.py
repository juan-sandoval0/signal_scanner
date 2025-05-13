import requests
from bs4 import BeautifulSoup

# Set browser headers to avoid getting blocked by websites
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

class Website:
    def __init__(self, url):
        self.url = url
        self.title = ""
        self.text = ""
        self.links = []
        self._scrape()

    def _scrape(self):
        try:
            # Request the HTML content of the page
            response = requests.get(self.url, headers=HEADERS)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Get the title
            self.title = soup.title.string.strip() if soup.title else "No title"

            # Remove irrelevant tags
            for tag in soup(["script", "style", "img", "input", "footer", "header", "nav"]):
                tag.decompose()

            # Get text
            body = soup.body
            if body:
                self.text = body.get_text(separator="\n", strip=True)
            else:
                self.text = ""

            # Collect all hyperlinks
            self.links = [a.get('href') for a in soup.find_all('a', href=True)]

        except Exception as e:
            print(f"[ERROR scraping {self.url}]: {e}")

    def summary(self):
        """
        Return a short summary
        """
        return {
            "url": self.url,
            "title": self.title,
            "num_links": len(self.links),
            "text_preview": self.text[:300] + "..." if len(self.text) > 300 else self.text
        }

    def get_text(self):
        """
        Return the full text.
        """
        return self.text
        