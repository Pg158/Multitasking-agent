import requests
import os

def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return "OPENWEATHER_API_KEY not found."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Failed to fetch weather. Status: {response.status_code}"

    data = response.json()

    try:
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
        return "Weather data format unexpected."
