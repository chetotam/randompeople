# TODO: migrate to Flask CLI instead of Flask-Script
'''This module enables command line interface for randompeople app.'''
from flask_script import Manager
from app import create_app

manager = Manager(create_app)

if __name__ == '__main__':
    manager.run()
