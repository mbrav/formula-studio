# Use the official Python image from the Docker Hub
FROM python:3.9-alpine
MAINTAINER Formula Studio

# Make a new directory to put our code in.
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . .

# Install dependencies
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev 
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .tmp-build-deps

EXPOSE 8000

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create user
RUN adduser -D user
USER user