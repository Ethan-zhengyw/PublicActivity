from model.activity import *
from model.user import *

def findUser(email):
    user = User.objects(email=email).first()
    return user

def findNotPassedActivities():
    result = Activity.objects(isPass=0).all()
    return result

def setPass(aid):
    result = Activity.objects(id=aid).first()
    result.isPass = 1
    result.save()

def setFailPass(aid):
    result = Activity.objects(id=aid).first()
    result.isPass = -1
    result.save()
