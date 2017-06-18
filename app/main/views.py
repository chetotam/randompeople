'''This module contains handler for main page of the application.'''
from flask import current_app

from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    '''Return main page.'''
    return current_app.send_static_file('index.html')
