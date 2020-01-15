import os

from waitress import serve

from app import app


port = os.getenv('PORT', 5000)
serve(app, listen=f'*:{port}')
