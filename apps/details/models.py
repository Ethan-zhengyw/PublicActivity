from model.user import *
from model.activity import *

def findActivityById(aid):
    result = Activity.objects(id=aid).first()
    return result
