# Use the official Python image from the Docker Hub
FROM python:3.9-alpine
MAINTAINER Formula Studio

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put our code in.
RUN mkdir /App
WORKDIR /App
COPY . /App

# Install dependencies
COPY ./requirements.txt /App/requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

# Create user
RUN adduser -D user
USER user