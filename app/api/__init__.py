'''This package contains randompeople app API.'''
from flask import Blueprint

api = Blueprint('api', __name__)

from . import v1
