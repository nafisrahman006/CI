FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade setuptools

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
