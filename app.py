from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Doug v1.0.1 says Hello, Docker!'
