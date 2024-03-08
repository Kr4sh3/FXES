from flask import Flask
import requests

app = Flask(__name__)

import smtplib, ssl

port = 465  # For SSL
password = "fsjs usqt yilj pwxu"

# Create a secure SSL context
context = ssl.create_default_context()

def send_str_to_email(str):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("fxes672@gmail.com", password)
        server.sendmail("fxes672@gmail.com", "pokemonjm@gmail.com", str)
    
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
    keywords = requests.get("https://fxes.onrender.com/api/searchterms").json()
    for tweet in unsent_tweets:
        user = requests.get(f"https://fxes.onrender.com/api/users/{tweet['associated_user']}").json()
        username = user['username']
        user_keywords = []
        for keyword in keywords:
            if keyword['associated_user'] == username:
                user_keywords.append(keyword['term'])
        if does_tweet_contain_keywords(tweet, user_keywords):
            str += username + ": " + tweet['text'] + " \n"
        tweet['email_notified'] = True
        requests.put(f"https://fxes.onrender.com/api/tweets/{tweet['id']}",tweet)
    if str != '':
        send_str_to_email(str)
    return str


def does_tweet_contain_keywords(text, keywords):
    for keyword in keywords:
        if keyword in text:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")