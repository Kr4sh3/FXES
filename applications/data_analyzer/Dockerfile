FROM python:3.12.2-slim-bullseye

WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind", "0.0.0.0:6000", "main:app"]