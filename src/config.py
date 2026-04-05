import os
from dotenv import load_dotenv

load_dotenv(".env.example")


class Settings:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = int(os.getenv("DB_PORT", "3306"))
    DB_NAME = os.getenv("DB_NAME", "weather_etl")
    DB_USER = os.getenv("DB_USER", "weather_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "weather_pass")

    @property
    def database_url(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


settings = Settings()
