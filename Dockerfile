FROM python:3.10.7-slim

RUN apt-get -y update && apt-get -y upgrade

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --no-cache "poetry==1.4.0" && poetry --version

COPY pyproject.toml poetry.lock ./

RUN apt-get install -y default-libmysqlclient-dev python3-dev gcc netcat
RUN pip3 install --no-cache mysqlclient

RUN poetry install --no-dev --no-root

WORKDIR /app/src/newsapp