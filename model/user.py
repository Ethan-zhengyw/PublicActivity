from mongoengine import *
import hashlib

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


def md5HashPwd(password):
    return hashlib.new('md5', password).hexdigest()
