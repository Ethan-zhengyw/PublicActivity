from mongoengine import *

connect('activity')

class Activity(Document):
    name = StringField(required=True)
    create_date = DateTimeField(required=True)
    start_date = DateTimeField(required=True)
    deadline = DateTimeField(required=True)
    introduction = StringField(required=True)
    host_id = StringField(required=True)
    tags = ListField()
