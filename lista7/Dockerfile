FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /bankapp
WORKDIR /bankapp

COPY requirements.txt /bankapp/

RUN pip install -r requirements.txt

COPY . /bankapp/
