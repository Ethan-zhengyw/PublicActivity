from mongoengine import *

connect('activity')

class Activity(Document):
    name = StringField(required=True)
    create_time = DateTimeField(required=True)
    start_time = DateTimeField(required=True)
    deadline = DateTimeField(required=True)
    introduction = StringField(required=True)
    host = StringField(required=True)
    tags = ListField()
    creater_id = StringField(required=True)
    location = StringField(required=True)
