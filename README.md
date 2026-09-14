# Проект "Atomic Habits" 
(с использованием Django Rest Framework + Celery + Redis + PostgreSQL + Docker)

## Подготовка

1. Скопируйте `.env.example` в `.env`:
   ```bash
   cp .env.example .env

## Запуск 

1. Запустить локальный сервер:
   ```bash
   python manage.py runserver

2. Запуск Docker:
   ```bash
   docker compose up --build

3. Остановка Docker:
   ```bash
   docker compose down
   
# Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).