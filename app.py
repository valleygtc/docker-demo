import os
import logging
from logging import FileHandler

from flask import Flask, request


app = Flask(__name__)


# INFO -> log file
if not os.path.isdir('log'):
    os.mkdir('log')
app.logger.setLevel(logging.INFO)
fh = FileHandler('log/access.log', encoding='utf-8')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
fh.setFormatter(formatter)
app.logger.addHandler(fh)


@app.route('/')
def handle_hello():
    ua = request.headers.get('User-Agent')
    app.logger.info('access from User-Agent: %s', ua)
    return 'Hello, World!'
