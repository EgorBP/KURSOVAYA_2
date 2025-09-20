FROM python:3.13-slim
LABEL authors="Egor"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY alembic.ini .
COPY alembic/ ./alembic/
COPY app/ ./app/

CMD alembic upgrade head && python -m app.add_first_admin_on_startup && python -m app.main
