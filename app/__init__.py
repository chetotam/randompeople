'''Root package of randompeople app.'''
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS

from .config import Config


db = MongoEngine()
cors = CORS()


def create_app(config=Config.DEFAULT):
    '''Create and set up Flask application instance.'''
    app = Flask(__name__)
    app.config.from_object(config.value)

    from .main import main
    app.register_blueprint(main)
    from .api import api
    app.register_blueprint(api, url_prefix='/api')

    db.init_app(app)
    cors.init_app(app)

    return app
