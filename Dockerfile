FROM python:3.9-alpine
MAINTAINER Formula Studio

ENV PYTHONUNBUFFERED 1

COPY ./backend/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /App
WORKDIR /App
COPY ./backend /App

RUN adduser -D user
USER user