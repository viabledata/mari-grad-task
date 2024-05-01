from flask import Flask

from route.v1 import v1
from config import config
from route.db_extension import db

FLASK_CFG = "dev"


def register_blueprints(app):
    app.register_blueprint(v1, url_prefix="/v1")


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    register_blueprints(app)
    return app
