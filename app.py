from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'It's over Anakin! I have the high ground!!!'
