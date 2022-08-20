FROM python:3.9

MAINTAINER Abbas Shaikh

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /E-SHOP
WORKDIR /E-SHOP
COPY ./E-SHOP /E-SHOP

RUN mkdir -p /media
RUN mkdir -p /static