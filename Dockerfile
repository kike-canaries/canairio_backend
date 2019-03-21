FROM python:3.6-alpine3.7

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add libpq postgresql-dev \
    && apk add build-base

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./
