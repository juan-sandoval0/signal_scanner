import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai = OpenAI()

MODEL = "gpt-4o-mini"

link_system_prompt = """You are provided with a list of links found on a startup's website.
Your job is to classify and select the ones that are most useful for creating a company overview.
This includes: About, Mission, Team, Product, Services, Blog, Solutions, Company, and Careers/Jobs pages.

Please respond in the following JSON format:

{
  "links": [
    {"type": "about", "url": "https://example.com/about"},
    {"type": "careers", "url": "https://example.com/jobs"}
  ]
}

Only include 3-4 links that you believe are the most relevant. Do not include links to Terms, Privacy, Contact, or external domains.
"""

def build_user_prompt(url, links):
    """
    Turn a list of scraped links into a prompt for GPT to classify.
    """
    prompt = f"The website URL is: {url}\nHere are all of the links found on the page:\n"
    prompt += "\n".join(links)
    prompt += "\n\nSelect the most relevant ones and respond in the required JSON format."
    return prompt

def classify_links(url, links):
    """
    Decide which links are most relevant for the company summary.
    """
    prompt = build_user_prompt(url, links)

    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": link_system_prompt},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )

    result = response.choices[0].message.content
    return json.loads(result)

def generate_markdown_brief(summary_dict: dict) -> str:
    """
    Generates a Markdown summary of the startup.
    """
    system_prompt = """You are an analyst at a top tier investment bank that writes company reports for analysts and investors. 
    You write thoroughly and comprehensively.
    Given website content and relevant articles, generate a clear report in Markdown with the following format:

##Company Snapshot
Short description using company name, and information on HQ, Founding, Founders, Employees, and latest funding. If any of these are not available, do not include them.

##Product & Technology
Insights from the product and what they offer.

##Market Opportunity and Traction
Signals from articles and website, if available.

##Competitive Landscape
Leverage your personal knowledge as an investment professional.

##Investment View 
Base case, upside drivers, key risks, milestones, etc.

##Bottom Line
Example: This startup has executed extraordinary early-stage growth, carving a data-moat in an underserved, high-margin niche: expert human work that trains and augments AI. With product-market fit proven and capital in hand, the next phase hinges on diversifying end-markets and defending its data advantage as larger incumbents move downstream. For growth-stage investors, valuation premium appears justified relative to other Gen-AI infrastructure plays, but monitoring customer concentration and regulatory momentum will be critical.
"""

    # Build the user prompt from the dictionary
    prompt = f"Company: {summary_dict['company_name']}\n"
    prompt += f"Homepage:\n{summary_dict['homepage']['text'][:1000]}\n\n"

    for sub in summary_dict.get("subpages", []):
        prompt += f"{sub['type'].capitalize()} Page:\n{sub['text'][:1000]}\n\n"

    # Add tech press mentions if present
    articles = summary_dict.get("techcrunch_articles", [])
    if articles:
        prompt += "\n\nPress Coverage:\n"
        for a in articles:
            prompt += f"Title: {a['title']}\nDate: {a['date']}\nText: {a['text'][:700]}\n\n"


    # Truncate to keep total under ~4000 tokens
    prompt = prompt[:5000]

    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

