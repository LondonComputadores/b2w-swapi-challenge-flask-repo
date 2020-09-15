from .db import db

class Planets(db.Document):
    id = db.IntField(required=True, unique=True)
    name = db.StringField(required=True, unique=True)
    climate = db.ListField(db.StringField(), required=True)
    terreain = db.ListField(db.StringField(), required=True)
    appearances = db.IntField(default=0)