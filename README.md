# 🌤️ Weather Data ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)

> A robust, automated ETL (Extract, Transform, Load) pipeline built with Python that fetches hourly weather data, processes it, and loads it into a local MySQL database. 
> **Developed as a portfolio project for a Junior Data Engineer position.**

## 📖 Project Overview

This project demonstrates the core Data Engineering lifecycle by automating the extraction of meteorological data. The pipeline interacts with the [Open-Meteo API](https://open-meteo.com/) to gather precise hourly metrics (such as temperature, apparent temperature, and relative humidity) for specific locations like Narva.

**Key Features:**
*   **Extract:** Fetches real-time and forecasted weather data using the `requests` library.
*   **Transform:** Cleans, formats, and structures the raw JSON data into DataFrames using `pandas`.
*   **Load:** Safely inserts the structured data into a MySQL database, preventing duplicates.
*   **Database Management:** Utilizes SQLAlchemy 2.0 as an ORM and Alembic for schema migrations.
*   **Containerization:** The MySQL database runs in an isolated Docker container for easy setup.

## 🛠️ Tech Stack

*   **Language:** Python 3.13
*   **Data Processing:** Pandas, Requests
*   **Database:** MySQL 8.0
*   **ORM & Migrations:** SQLAlchemy 2.0, Alembic
*   **Infrastructure:** Docker Compose, python-dotenv

## 📁 Project Structure

```text
weather-etl-project/
├── alembic/                # Database migration configuration and scripts
├── src/
│   ├── etl/
│   │   ├── extract.py      # API data extraction logic
│   │   ├── transform.py    # JSON to DataFrame transformation
│   │   └── load.py         # MySQL database loading logic
│   ├── models/             # SQLAlchemy ORM models
│   └── main.py             # Main ETL execution script
├── .env                    # Environment variables (DB credentials)
├── docker-compose.yml      # Docker configuration for MySQL
├── alembic.ini             # Alembic configuration
└── requirements.txt        # Python dependencies
```

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.13+** and **Docker Desktop** installed on your machine.

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/weather-etl-project.git
cd weather-etl-project
```

### 2. Set up the environment
Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
pip install -r requirements.txt
```

### 3. Start the Database
Spin up the MySQL container using Docker Compose:
```bash
docker compose up -d
```

### 4. Run Database Migrations
Create the `weather_hourly` table by running Alembic migrations:
```bash
alembic upgrade head
```

### 5. Execute the ETL Pipeline
Run the main script to fetch and load the weather data:
```bash
python -m src.main
```

## 📊 Data Analytics (PopSQL / MySQL)

Once the data is loaded, you can run analytical queries to uncover weather trends. Here are a few examples you can run using tools like PopSQL or MySQL Workbench:

**Check total loaded rows:**
```sql
SELECT COUNT(*) as total_rows FROM weather_hourly;
```

**View recent weather data:**
```sql
SELECT 
    city,
    forecast_time,
    temperature_2m,
    relative_humidity_2m,
    apparent_temperature
FROM weather_hourly
ORDER BY forecast_time DESC
LIMIT 10;
```

**Calculate daily temperature statistics:**
```sql
SELECT 
    DATE(forecast_time) as day,
    ROUND(AVG(temperature_2m), 1) as avg_temp,
    ROUND(MIN(temperature_2m), 1) as min_temp,
    ROUND(MAX(temperature_2m), 1) as max_temp
FROM weather_hourly
GROUP BY DATE(forecast_time)
ORDER BY day;
```

## 🗺️ Roadmap & Future Improvements

- [ ] Add support for dynamic city lists (extracting data for multiple locations).
- [ ] Set up pipeline orchestration (e.g., Apache Airflow or simple Cron jobs).
- [ ] Build a REST API using **FastAPI** to serve the collected weather data.
- [ ] Implement robust error handling and tracking using the Python `logging` module.

---
*Created by [Your Name](https://github.com/YOUR_USERNAME) - Feel free to reach out for feedback or collaboration!*