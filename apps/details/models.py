from model.user import *
from model.activity import *

def findActivityById(aid):
    result = Activity.objects(id=aid).first()
    return result

def findUserByEmail(email):
    return User.objects(email=email).first()

def checkPar(email, aid):
    user = User.objects(email=email).first()

    if aid in user.participate:
        return True
    else:
        return False


def checkCon(email, aid):
    user = User.objects(email=email).first()

    if aid in user.concern:
        return True
    else:
        return False

