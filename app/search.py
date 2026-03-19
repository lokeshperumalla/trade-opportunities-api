from duckduckgo_search import DDGS

def search_sector_news(sector: str):

    query = f"{sector} sector India market news"

    results = []

    try:

        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r["body"])

    except Exception as e:
        results.append("Unable to fetch latest news.")

    return results