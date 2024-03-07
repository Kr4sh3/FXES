from flask import Flask
import requests
from tweety import Twitter
from flask_apscheduler import APScheduler
from datetime import datetime, date
import json

import redis
from rq import Worker, Queue, Connection
conn = redis.from_url("redis://red-cnksjben7f5s73b1v9q0:6379")
q = Queue(connection=conn)
def print_test():
    print("test")
job = q.enqueue_call(func=print_test, result_ttl=5000)

app = Flask(__name__)
scheduler = APScheduler()
twitter_session = Twitter("session")

@app.route('/')
def index():
    return 'This is the route for the data collector!'

@scheduler.task('interval', id='get_tweets', hours=24)
def get_tweets():
    # Login
    twitter_session.start("scrapertestzWm", "zWmAYotd&!t$mR38")
    # Request list of users to retrieve tweets for
    users = requests.get("https://fxes.onrender.com/api/users").json()
    for user in users:
        username = user['username']
        # Scrape twitter user for tweets with tweety
        tweets = twitter_session.get_tweets(username)
        for tweet in tweets:
            if hasattr(tweet, "text"):
                # Build a json object and send it over REST to django web app
                tweet_obj = {
                    "text": tweet['text'],
                    "associated_user": user['id'],
                    "date": datetime.today()
                }
                jsonstr_tweet = json.dumps(tweet_obj, default=json_serial)
                json_tweet = json.loads(jsonstr_tweet)
                requests.post("https://fxes.onrender.com/api/tweets", json=json_tweet)

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()

    app.run(debug=True, host="0.0.0.0")
else:
    scheduler.start()