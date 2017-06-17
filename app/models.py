'''This module defines application data models.'''
from . import db


class Member(db.EmbeddedDocument):
    '''Represents person, participating in this random thing.'''

    name = db.StringField(unique=True, required=True)
    #email = db.StringField(unique=True, required=True)

    def __init__(self, *, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def __repr__(self):
        return '<Member {}>'.format(self.name)


class Room(db.Document):
    '''Represents group of members to choose from.'''

    meta = {'collection': 'rooms'}

    name = db.StringField(unique=True, required=True)
    members = db.SortedListField(db.EmbeddedDocumentField(Member), ordering='name')

    def __init__(self, *, name, members, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.members = members

    def __repr__(self):
        return '<Room {}>'.format(self.name)
