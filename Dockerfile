FROM python:3.9-alpine

ENV PYTHONUNBUFERRED 1

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user