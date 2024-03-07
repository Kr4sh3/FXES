from flask import Flask
import requests
import redis
from rq import Worker, Queue, Connection

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the route for the data analyzer!'

@app.route('/run_analysis')
def run_analysis():
    return "test"

listen = ['default']
redis_url = "redis://red-cnksjben7f5s73b1v9q0:6379"
conn = redis.from_url(redis_url)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")