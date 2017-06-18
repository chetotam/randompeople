'''This package contains randompeople app API v1.'''
from .. import api
from .rooms import Rooms
from .members import Members

room_view = Rooms.as_view('rooms')
api.add_url_rule(
    '/v1/rooms/',
    defaults={'room_name': None},
    view_func=room_view,
    methods=['GET', 'POST', 'DELETE'])
api.add_url_rule(
    '/v1/rooms/<string:room_name>',
    view_func=room_view,
    methods=['GET', 'DELETE'])

member_view = Members.as_view('members')
api.add_url_rule(
    '/v1/rooms/<string:room_name>/members/',
    defaults={'member_name': None},
    view_func=member_view,
    methods=['GET', 'DELETE'])
api.add_url_rule(
    '/v1/rooms/<string:room_name>/members/',
    view_func=member_view,
    methods=['POST',])
api.add_url_rule(
    '/v1/rooms/<string:room_name>/members/<string:member_name>',
    view_func=member_view,
    methods=['GET', 'DELETE'])
