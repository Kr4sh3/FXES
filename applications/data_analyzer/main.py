from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the route for the data analyzer!'

@app.route('/run-analysis')
def run_analysis():
    tweets = requests.get("https://fxes.onrender.com/api/tweets").json()
    unsent_tweets = []
    for tweet in tweets:
        if tweet['email_notified'] == False:
            unsent_tweets.append(tweet)
    str = ''
    for tweet in unsent_tweets:
        user = requests.get(f"https://fxes.onrender.com/api/users/{tweet['associated_user']}").json()
        username = user['username']
        str += username + ": " + tweet['text'] + " \n"
    return str

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")