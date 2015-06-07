from mongoengine import *

connect('activity')

class User(Document):
    username = StringField(required=True, unique=True)
    password = StringField(required=True)
    email = EmailField(required=True)
    user_type = IntField(required=True)
    introduction = StringField()
    avatar = StringField()
    gender = IntField()
    hobby = StringField()
    tags = ListField()
