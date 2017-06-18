# TODO: migrate to Flask CLI instead of Flask-Script
'''This module enables command line interface for randompeople app.'''
from flask_script import Manager
from app import create_app, db
from app.models import Room, Member

app = create_app()
manager = Manager(app)

@manager.shell
def make_shell_context():
    ''''''
    return dict(app=app, db=db, Room=Room, Member=Member)

if __name__ == '__main__':
    manager.run()
