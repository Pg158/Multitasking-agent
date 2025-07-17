import os
from dotenv import load_dotenv

from llama_index.llms.groq import Groq
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.tools import FunctionTool

from tools.google_search import google_search
from tools.youtube_search import youtube_search
from tools.weather_tool import get_weather

load_dotenv()

llm = Groq(model="llama3-70b-8192", temperature=0.1)

tools = [
    FunctionTool.from_defaults(fn=google_search, name="google_search", description="Search Google."),
    FunctionTool.from_defaults(fn=youtube_search, name="youtube_search", description="Search YouTube."),
    FunctionTool.from_defaults(fn=get_weather, name="get_weather", description="Get current weather."),
]

agent = FunctionAgent.from_tools(
    tools=tools,
    llm=llm,
    system_prompt="""
You are a smart and articulate multi-tool AI assistant with access to the following tools:

1. `google_search(query: str)` — Use this to look up current topics, definitions, websites, or factual questions.
2. `youtube_search(query: str)` — Use this to find top YouTube videos related to tutorials, topics, or reviews.
3. `get_weather(city: str)` — Use this to fetch live weather information for a given city.

When answering:
- Use the most relevant tool based on the user's query.
- Extract the most useful, human-readable information from the tool output.
- Rephrase the tool's output in a polished, helpful tone.
- Always give clean formatting, include bullet points if multiple results are returned.
- If a tool fails or data is missing, explain that gracefully.
- If no tool is needed, answer directly using your own knowledge.

Examples:
- For Google results, highlight the top result and mention the link clearly.
- For YouTube videos, list the video titles and links nicely.
- For weather info, include emojis and units, and structure the data clearly.

Stay conversational, concise, and helpful in tone. Always assume the user is non-technical.

""",
    verbose=True
)
