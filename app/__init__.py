'''Root package of randompeople app.'''
from flask import Flask
from .config import Config

def create_app(config=Config.DEFAULT):
    '''Create and set up Flask application instance.'''
    app = Flask(__name__)
    app.config.from_object(config.value)

    from .main import main
    app.register_blueprint(main)

    return app
