# tools/google_search.py

from serpapi import GoogleSearch
import streamlit as st

def google_search(query: str) -> str:
    api_key = st.secrets["SERPAPI_API_KEY"]

    params = {
        "q": query,
        "api_key": api_key,
        "engine": "google",
        "num": 3  # limit to 3 results
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict()

        if "organic_results" not in results:
            return "❌ No results found."

        output = "🔍 Top Google Results:\n"
        for res in results["organic_results"][:3]:
            title = res.get("title", "No Title")
            link = res.get("link", "")
            output += f"- [{title}]({link})\n"

        return output

    except Exception as e:
        return f"⚠️ Google Search failed: {str(e)}"
