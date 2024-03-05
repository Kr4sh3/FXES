FROM python:3.12.2-slim-bullseye

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY . .

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "FXES.wsgi:application"]