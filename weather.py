import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
       
def fetch_weather(city):
    params = {"q": city, "units": "metric", "appid": API_KEY}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Couldn't connect. Check your internet.")
        return None
    if response.status_code == 404:
        print(f"City '{city}' not found. Check the spelling.")
    elif response.status_code == 401:
        print("Invalid API key. It may not be active yet.")
    elif response.status_code == 429:
        print("Too many requests. Wait a minute and try again.")
    elif response.status_code != 200:
        print(f"Something went wrong (status {response.status_code}).")
    else:
        return response.json()
    return None

def parse_weather(data):
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "wind": data["wind"]["speed"],
    }
