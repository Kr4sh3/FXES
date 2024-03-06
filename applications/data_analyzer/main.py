from flask import Flask
import requests

from flask_apscheduler import APScheduler

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the route for the data analyzer!'

if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()

    app.run(debug=True, host="0.0.0.0")


@scheduler.task('cron', id='get_tweets', week='*', day_of_week='sun')
def get_tweets():
    users = requests.get("https://fxes.onrender.com/api/users")