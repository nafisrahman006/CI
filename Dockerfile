FROM python:alpine

RUN apk add --no-cache gcc musl-dev libffi-dev

RUN pip install --no-cache-dir --upgrade setuptools==75.8.0

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .
