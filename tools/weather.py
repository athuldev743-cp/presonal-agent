import requests
from config import OPENWEATHER_API_KEY

def get_weather(city_name: str):
    """
    Fetch current weather for the given city.
    """
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            return "Sorry, I couldn't find the weather for that location."

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (f"Weather in {city_name}:\n"
                f"Description: {weather}\n"
                f"Temperature: {temp}°C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s")

    except Exception as e:
        return "Sorry, I couldn’t fetch the weather right now."
