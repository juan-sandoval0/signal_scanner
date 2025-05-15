# Startup Signal Scanner

Generates an investor-style startup brief from any company website using GPT-4o, BeautifulSoup, and web data.

> Exploring AI application design, information extraction, and insights from public data.

---

## What It Does

Lets you input the URL of any startup’s website and returns a clean, investor-friendly brief by:

- Scraping the landing page and important subpages (like About, Team, Careers)
- Classifying relevant links using OpenAI API
- Extracting TechCrunch articles using Google + BeautifulSoup
- Generating a summary report using GPT-4o

I wanted to simulate how an analyst or early-stage investor might summarize the company at a glance.

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

### 1. Clone the repo
### 2. Set up your environment
### Add API Keys
> OPENAI_API_KEY=your-openai-key
> SERPAPI_API_KEY=your-serpapi-key

---

## My future ideas
- Integrate GitHub, Product Hunt, or Google Trends for better analysis
- Add Streamlit front-end for interactive reports
- Auto-export reports to PDF
