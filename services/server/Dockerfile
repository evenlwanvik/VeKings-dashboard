FROM python:3.9.5-slim-buster

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn.sh"]