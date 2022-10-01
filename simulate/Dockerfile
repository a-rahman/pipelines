FROM python:3.8-slim

RUN pip install requests && pip install responses

COPY wait.sh wait.sh
RUN chmod 777 wait.sh

CMD wait.sh 127.0.0.1 5000 && python simulator.py