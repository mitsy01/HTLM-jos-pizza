import os

import requests
from dotenv import load_dotenv

load_dotenv()

def get_wheather(city: str = "Kharkiv"):
    api_key = os.getenv("WHEATHER_API")
    url = f"'https://api.weatherapi.com/v1/current.json?q={city}&key={api_key}"
    responce = requests.get(url).json()
    wheather = {
        "temp": responce.get("current", {}).get("temp_c"),
        "text": responce.get("current", {}).get("condition", {}).get("text"),
        "icon": responce.get("current", {}).get("condition", {}).get("icon"),
        "city": city
    }
    return wheather