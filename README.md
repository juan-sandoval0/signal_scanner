# Startup Signal Scanner

Generate investor-style startup briefs from any company website using GPT-4o, BeautifulSoup, and web data.

> A project by Juan Sandoval to explore AI application design, information extraction, and strategic insights from public data.

---

## What It Does

Lets you input the URL of any startup’s website and returns a clean, investor-friendly Markdown brief by:

- Scraping the landing page and important subpages (like About, Team, Careers)
- Classifying relevant links using OpenAI API
- Extracting TechCrunch articles using Google + BeautifulSoup
- Generating a summary report using GPT-4o

The output is a structured Markdown report designed to simulate how an analyst or early-stage investor might summarize the company at a glance.

---

## Tech Stack

- **Python**
- **Jupyter Notebook**
- `openai` for GPT-4o
- `beautifulsoup4` for HTML parsing
- `requests` for web scraping
- `serpapi` for Google Search-based scraping

---

## How to Run

### Clone the repo

```bash
git clone https://github.com/yourusername/startup-signal-scanner.git
cd startup-signal-scanner

### Set up your environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### Add API Keys
OPENAI_API_KEY=your-openai-key
SERPAPI_API_KEY=your-serpapi-key

## My future ideas
 Future Ideas
Integrate GitHub, Product Hunt, or Google Trends for better analysis
Add Streamlit front-end for interactive reports
Auto-export reports to PDF
