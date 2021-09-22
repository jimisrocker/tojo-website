from . import db

class Business(db.Document):
    name=db.StringField()
    email=db.StringField()
    phone=db.StringField()
    message=db.StringField()

class Message(db.Document):
    name=db.StringField()
    email=db.StringField()
    message=db.StringField()
