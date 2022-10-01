FROM python:3.8-slim

RUN pip install Flask && pip install kafka-python

COPY wait.sh wait.sh
RUN chmod 777 wait.sh

CMD wait.sh 127.0.0.1 9092 && python proxy.py