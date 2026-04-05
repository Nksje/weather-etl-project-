# Weather ETL Project

ETL-проект для портфолио Junior Data Engineer.

## Стек

- Python
- MySQL
- SQLAlchemy
- Alembic
- Pandas
- Docker Compose

## Что делает

1. Забирает погодные данные из Open-Meteo.
2. Преобразует JSON в табличный формат.
3. Загружает данные в MySQL.
4. Поддерживает миграции через Alembic.

## Запуск

```bash
docker compose --env-file .env.example up -d
```
