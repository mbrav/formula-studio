# Use the official Python image from the Docker Hub
FROM python:3.9-alpine
MAINTAINER Formula Studio

# ENV
ENV WORK_DIR="/usr/src/app"
ENV USER_NAME=user
# Make sure we use the virtualenv:
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Make a new directory to put our code in.
RUN mkdir $WORK_DIR
WORKDIR $WORK_DIR
COPY . .

# Install dependencies
RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    postgresql-dev gcc python3-dev musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .tmp-build-deps

# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create user and give permissions
RUN adduser -D $USER_NAME
RUN chown -R $USER_NAME:$USER_NAME $WORK_DIR && \
    chmod -R 755 $WORK_DIR && \
    chown -R $USER_NAME:$USER_NAME /opt/venv/ && \
    chmod -R 755 /opt/venv/
USER $USER_NAME

EXPOSE 8000