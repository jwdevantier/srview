from flask import Flask
import logging
import coloredlogs

def make_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "s3cr3t!"
    return app

app = make_app()
logger = logging.getLogger("flask-app")

from srview import views