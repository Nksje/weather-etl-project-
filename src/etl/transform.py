import pandas as pd


def transform_weather(payload: dict, city: str) -> pd.DataFrame:
    hourly = payload["hourly"]

    df = pd.DataFrame({
        "forecast_time": pd.to_datetime(hourly["time"]),
        "temperature_2m": hourly.get("temperature_2m", []),
        "relative_humidity_2m": hourly.get("relative_humidity_2m", []),
        "apparent_temperature": hourly.get("apparent_temperature", []),
    })

    df["city"] = city
    df["latitude"] = payload["latitude"]
    df["longitude"] = payload["longitude"]

    return df[
        [
            "city",
            "latitude",
            "longitude",
            "forecast_time",
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
        ]
    ]
