from datetime import datetime
from sqlalchemy import DateTime, Float, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
from src.db import Base


class WeatherHourly(Base):
    __tablename__ = "weather_hourly"
    __table_args__ = (
        UniqueConstraint("city", "forecast_time",
                         name="uq_city_forecast_time"),
    )

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    city: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    forecast_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, index=True)

    temperature_2m: Mapped[float | None] = mapped_column(Float, nullable=True)
    relative_humidity_2m: Mapped[float |
                                 None] = mapped_column(Float, nullable=True)
    apparent_temperature: Mapped[float |
                                 None] = mapped_column(Float, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
