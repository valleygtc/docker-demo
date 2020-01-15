from flask import Flask


app = Flask(__name__)


@app.route('/')
def handle_hello():
    return 'Hello, World!'
