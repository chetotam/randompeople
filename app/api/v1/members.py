'''This module contains handlers to Members API v1 requests.'''
from random import sample

from flask import abort, jsonify, request
from flask.views import MethodView

from ... import db
from ...models import Member, Room


class Members(MethodView):
    '''Handles Members API v1 GET, POST and DELETE requests.'''

    def get(self, room_name, member_name):
        '''Return specified member from specified room as JSON.'''
        try:
            room_exists = Room.objects.get(name=room_name)
        except db.DoesNotExist:
            abort(404)

        if request.args.get('random'):
            total_members = room_exists.members.count()
            try:
                number_of_winners = min(int(request.args.get('random')), total_members)
            except ValueError:
                abort(400)
            winners = []
            for i in sample(range(0, total_members), number_of_winners):
                winners.append(room_exists.members[i])
            return jsonify(winners), 201

        if member_name is None:
            return jsonify(room_exists.members), 201
        else:
            try:
                member_exists = room_exists.members.get(name=member_name)
                return jsonify(member_exists), 201
            except db.DoesNotExist:
                abort(404)

    def post(self, room_name):
        '''Add new member to specified room.'''
        try:
            room_exists = Room.objects.get(name=room_name)
        except db.DoesNotExist:
            abort(404)

        if not request.get_json() or not 'name' in request.get_json():
            abort(400)

        new_member = Member(name=request.get_json()['name'].strip())
        try:
            member_exists = room_exists.members.get(name=new_member.name)
            return jsonify(member_exists), 409
        except db.DoesNotExist:
            room_exists.update(add_to_set__members=new_member)

        return jsonify(new_member), 201

    def delete(self, room_name, member_name):
        '''Delete specified member from specified room.'''
        try:
            room_exists = Room.objects.get(name=room_name)
        except db.DoesNotExist:
            abort(404)

        if member_name is None:
            room_exists.members = []
            room_exists.save()
            return 204
        else:
            try:
                member_exists = room_exists.members.get(name=member_name)
                room_exists.update(pull__members__name=member_exists.name)
                return 204
            except db.DoesNotExist:
                abort(404)
