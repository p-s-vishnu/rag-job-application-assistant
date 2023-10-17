FROM python:3.9-slim-buster

WORKDIR /web
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /web
RUN pip install --upgrade pip