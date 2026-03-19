from google import genai
import os
from dotenv import load_dotenv

load_dotenv()


def analyze_market(sector, news):

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    news_text = "\n".join(news)

    prompt = f"""
You are a financial market analyst.

Analyze the Indian {sector} sector using the following news:

{news_text}

Generate a structured markdown report:

# {sector.capitalize()} Sector Market Analysis

## Market Overview
## Key Trends
## Trade Opportunities
## Risks
## Conclusion
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"# Error\nUnable to generate analysis: {str(e)}"