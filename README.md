# Weather ETL Pipeline 🌦️

A portfolio project for a **Junior Data Engineer** position. This is an automated ETL pipeline built with Python that extracts hourly weather data from the [Open-Meteo API](https://open-meteo.com/), transforms it, and loads it into a local MySQL database.

## 🎯 About the Project

This project demonstrates the core Data Engineering lifecycle (ETL):
- **Extract** — Fetches raw weather data for specified coordinates using a public REST API.
- **Transform** — Cleans the JSON response, normalizes timestamps, and converts the data into a tabular format using `pandas`.
- **Load** — Performs an incremental load of the cleaned data into a relational MySQL database (with duplicate prevention).
- **Schema Management** — Manages database schema versioning and migrations using SQLAlchemy and Alembic.

Currently, the pipeline collects hourly temperature (`temperature_2m`), relative humidity (`relative_humidity_2m`), and apparent temperature (`apparent_temperature`) for Narva, Estonia.

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Data Processing:** Pandas, Requests
- **Database:** MySQL 8.0
- **ORM & Migrations:** SQLAlchemy 2.0, Alembic
- **Infrastructure:** Docker Compose, python-dotenv

## 📂 Project Structure

```text
weather-etl-project/
├── alembic/                # Database migration scripts and config
├── src/
│   ├── etl/
│   │   ├── extract.py      # Extracts data from Open-Meteo API
│   │   ├── transform.py    # Transforms JSON response into a DataFrame
│   │   └── load.py         # Loads processed data into MySQL
│   ├── models/
│   │   └── weather.py      # SQLAlchemy ORM model for weather_hourly table
│   ├── config.py           # Environment variables configuration
│   ├── db.py               # Database connection and session setup
│   └── main.py             # Entry point to trigger the ETL pipeline
├── .env.example            # Environment variables template
├── docker-compose.yml      # Docker configuration for MySQL
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
