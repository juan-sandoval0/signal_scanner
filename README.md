# Startup Signal Scanner

Generates a brief on any startup from any company website using GPT-4o, BeautifulSoup, and web data!

---

## What It Does

Lets you input the URL of any startup’s website and returns a brief by:

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
### Add API Keys for OpenAI and SERPAI

---

## My future ideas
- Integrate GitHub, Product Hunt, or Google Trends for better analysis
- Add Streamlit front-end
- Auto-export reports to PDF
