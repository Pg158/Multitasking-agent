import os
from googleapiclient.discovery import build

def youtube_search(query: str) -> str:
    api_key = os.getenv("YOUTUBE_API_KEY")
    if not api_key:
        return "YOUTUBE_API_KEY not found."

    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.search().list(q=query, part="snippet", type="video", maxResults=3)
        response = request.execute()

        results = []
        for item in response["items"]:
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            link = f"https://www.youtube.com/watch?v={video_id}"
            results.append(f"{title}\n{link}")

        return "\n\n".join(results)

    except Exception as e:
        return f"Error fetching YouTube results: {e}"

