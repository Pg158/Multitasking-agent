import requests
import streamlit as st

def get_weather(city: str) -> str:
    api_key = st.secrets["OPENWEATHER_API_KEY"]

    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )
    
    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return f"❌ Failed to fetch weather. Status: {response.status_code}"

        data = response.json()

        desc = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        return (
            f"🌤️ Weather in {city.title()}:\n"
            f"- Condition: {desc}\n"
            f"- Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind Speed: {wind} m/s"
        )

    except (KeyError, IndexError):
        return "⚠️ Unexpected weather data format."

    except Exception as e:
        return f"⚠️ Error retrieving weather: {str(e)}"

