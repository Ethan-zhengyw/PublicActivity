from mongoengine import *
import hashlib

connect('activity')

class User(Document):
    username = StringField(unique=True)
    password = StringField(required=True)
    email = EmailField(required=True, unique=True)
    user_type = IntField()
    introduction = StringField()
    avatar = StringField()
    gender = IntField()
    tags = StringField()

    concern = ListField()
    participate = ListField()
    create = ListField()


def md5HashPwd(password):
    return hashlib.new('md5', password).hexdigest()
