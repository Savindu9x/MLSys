# Specify Base Image from the DockerHub
FROM python:alpine3.19

# set /app as the working directory
WORKDIR /app
# Docker works in layers, any file that has not changed will be cached.
COPY requirements.txt .

RUN pip3 install -r requirements.txt


# copy content in local src folder to /app directory within the container.
COPY ./src .

# base directory
# |
# -- src
# ----- | sourcecode
# -- Dockerfile

EXPOSE 8501

