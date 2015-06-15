from model.activity import *
def findNotPassedActivities():
	result = Activity.objects(isPass=0).all()
	return result

def setPass(aid):
	result = Activity.objects(id=aid).first()
	result.isPass = 1
	result.save()