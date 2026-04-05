from sqlalchemy import select
from src.db import SessionLocal
from src.models.weather import WeatherHourly


def load_weather(df) -> int:
    inserted = 0

    with SessionLocal() as session:
        for row in df.to_dict(orient="records"):
            exists = session.execute(
                select(WeatherHourly.id).where(
                    WeatherHourly.city == row["city"],
                    WeatherHourly.forecast_time == row["forecast_time"].to_pydatetime(
                    ),
                )
            ).scalar_one_or_none()

            if exists:
                continue

            weather_row = WeatherHourly(
                city=row["city"],
                latitude=float(row["latitude"]),
                longitude=float(row["longitude"]),
                forecast_time=row["forecast_time"].to_pydatetime(),
                temperature_2m=float(
                    row["temperature_2m"]) if row["temperature_2m"] is not None else None,
                relative_humidity_2m=float(
                    row["relative_humidity_2m"]) if row["relative_humidity_2m"] is not None else None,
                apparent_temperature=float(
                    row["apparent_temperature"]) if row["apparent_temperature"] is not None else None,
            )
            session.add(weather_row)
            inserted += 1

        session.commit()

    return inserted
