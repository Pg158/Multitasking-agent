from serpapi import GoogleSearch
import os

def google_search(query: str) -> str:
    api_key = os.getenv("SERPAPI_API_KEY")
    if not api_key:
        return "SERPAPI_API_KEY not found."

    params = {"q": query, "api_key": api_key, "engine": "google", "num": 3,}

    search = GoogleSearch(params)
    results = search.get_dict()
    true_results = results.get("true_results", [])

    if not true_results:
        return "No results found."

    top_links = [
        f"{r.get('title', 'No title')}\n{r.get('link', 'No link')}"
        for r in true_results[:3]
    ]

    return "\n\n".join(top_links)
