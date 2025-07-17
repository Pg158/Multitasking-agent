# 🤖 Multi-Tool AI Assistant

A Streamlit web app powered by **LlamaIndex**, **Groq**, and multiple external APIs to help you:

- 🔍 Perform Google Searches
- 🌦️ Get real-time Weather Information
- 📺 Search YouTube videos

---

## 🚀 Live Demo

👉 [Try it now on Streamlit](https://multitasking-agent.streamlit.app)

---

## 🛠️ Built With

- [Streamlit](https://streamlit.io/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [Groq LLaMA3-70B](https://console.groq.com/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [YouTube Data API](https://developers.google.com/youtube/v3)
- [SerpAPI](https://serpapi.com/)

---

## 🧠 How It Works

This app uses a **FunctionCallingAgent** from LlamaIndex. It intelligently selects and invokes the correct tool based on your query:

- `"What is the weather in Tokyo?"` → Weather Tool  
- `"Show me YouTube videos on LlamaIndex"` → YouTube Tool  
- `"What is RAG in AI?"` → Google Search Tool  

---

## 🔧 Setup Instructions (for local testing)

1. Clone this repo:
   ```bash
   git clone https://github.com/pg158/multitasking-agent.git
   cd multitasking-agent
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a .env file or configure secrets.toml if testing locally:
    ```bash
    GROQ_API_KEY=your_groq_key
    OPENWEATHER_API_KEY=your_weather_key
    YOUTUBE_API_KEY=your_youtube_key
    SERPAPI_API_KEY=your_serpapi_key
    ```

4. Run locally:
    ```bash
    streamlit run app.py
    ```

---

## 📁 Project Structure

    multitasking-agent/
    ├── app.py
    ├── agent_core.py
    ├── tools/
    │   ├── google_search.py
    │   ├── youtube_search.py
    │   └── weather_tool.py
    ├── requirements.txt
    ├── .gitignore
    └── .streamlit/
        └── secrets.toml

---

## 📜 License
This project is licensed under the MIT License.