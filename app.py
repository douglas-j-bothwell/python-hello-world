from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Doug 1.0.15 says Hello, Docker!'
