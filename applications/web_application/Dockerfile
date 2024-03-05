FROM python:3.12.2-slim-bullseye

WORKDIR /

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python manage.py makemigrations tweets
RUN python manage.py migrate tweets

CMD [ "gunicorn", "--bind", "0.0.0.0:80", "FXES.wsgi:application"]