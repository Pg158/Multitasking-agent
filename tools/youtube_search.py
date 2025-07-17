# tools/youtube_search.py

import requests
import streamlit as st

def youtube_search(query: str) -> str:
    api_key = st.secrets["YOUTUBE_API_KEY"]

    url = (
        f"https://www.googleapis.com/youtube/v3/search"
        f"?part=snippet&q={query}&type=video&maxResults=3&key={api_key}"
    )

    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return f"❌ Failed to fetch YouTube results. Status: {response.status_code}"

        results = response.json()

        if "items" not in results:
            return "❌ No results found."

        output = "📺 Top YouTube Videos:\n"
        for item in results["items"]:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            link = f"https://www.youtube.com/watch?v={video_id}"
            output += f"- [{title}]({link})\n"

        return output

    except Exception as e:
        return f"⚠️ YouTube Search failed: {str(e)}"
