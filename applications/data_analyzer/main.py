from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the route for the data analyzer!'

@app.route('/run-analysis')
def run_analysis():
    return "test"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")