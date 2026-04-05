import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"


def fetch_weather(latitude: float, longitude: float) -> dict:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,relative_humidity_2m,apparent_temperature",
        "timezone": "auto",
        "forecast_days": 3,
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()
