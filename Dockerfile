FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev python3 python3-pip build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 base_webhook.py
