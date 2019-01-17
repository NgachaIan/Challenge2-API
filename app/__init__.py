'''Creating app'''
import os
from flask import Flask
from instance.config import app_config
"""importing the configurations from the .config file which is in the instance folder"""


def create_app():
    '''creating  the app using the configurations in the dictionary created in the .config file'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config["development"])
    app.config.from_pyfile('config.py')
    from .api.version1.views import version1 as v1
    app.register_blueprint(v1)
    return app
