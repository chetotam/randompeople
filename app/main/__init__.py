'''This package contains core app functionality.'''
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
