'''This module contains handlers to Rooms API v1 requests.'''
from flask import abort, jsonify, request
from flask.views import MethodView

from ... import db
from ...models import Room


class Rooms(MethodView):
    '''Handles Rooms API v1 GET, POST and DELETE requests.'''

    def get(self, room_name):
        '''Return specified room as JSON.'''
        if room_name is None:
            return jsonify(Room.objects), 200
        else:
            try:
                room_exists = Room.objects.get(name=room_name)
                return jsonify(room_exists), 200
            except db.DoesNotExist:
                abort(404)

    def post(self):
        '''Add new room.'''
        if not request.json or not 'name' in request.json:
            abort(400)

        new_room = Room(name=request.json['name'].strip(), members=[])
        try:
            room_exists = Room.objects.get(name=new_room.name)
            return jsonify(room_exists), 409
        except db.DoesNotExist:
            new_room.save()
            return jsonify(new_room), 201

    def delete(self, room_name):
        '''Delete specified room.'''
        if room_name is None:
            Room.drop_collection()
            return 'no content', 204

        try:
            Room.objects.get(name=room_name).delete()
            return 'no content', 204
        except db.DoesNotExist:
            abort(404)
