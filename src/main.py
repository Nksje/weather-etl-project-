from src.etl.extract import fetch_weather
from src.etl.transform import transform_weather
from src.etl.load import load_weather


def run():
    city = "Narva"
    latitude = 59.3772
    longitude = 28.1903

    payload = fetch_weather(latitude, longitude)
    df = transform_weather(payload, city)
    inserted = load_weather(df)

    print(f"Inserted rows: {inserted}")


if __name__ == "__main__":
    run()
