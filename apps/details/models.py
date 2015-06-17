from model.user import *
from model.activity import *

def findActivityById(aid):
    result = Activity.objects(id=aid).first()
    return result

def findUserByEmail(email):
    return User.objects(email=email).first()

def checkPar(email, aid):
    user = findUserByEmail(email)

    if aid in user.participate:
        return True
    else:
        return False


def checkCon(email, aid):
    user = findUserByEmail(email)

    if aid in user.concern:
        return True
    else:
        return False


def setPar(email, aid):
    user = findUserByEmail(email)
    activity = Activity.objects(id=aid).first()

    user.participate.append(aid)
    activity.participate.append(user.id)

    user.save()
    activity.save()

def setCon(email, aid):
    user = findUserByEmail(email)
    activity = Activity.objects(id=aid).first()

    user.concern.append(aid)
    activity.concern.append(user.id)

    user.save()
    activity.save()

def unsetPar(email, aid):
    user = findUserByEmail(email)
    activity = Activity.objects(id=aid).first()

    user.participate.remove(aid)
    activity.participate.remove(user.id)

    user.save()
    activity.save()

def unsetCon(email, aid):
    user = findUserByEmail(email)
    activity = Activity.objects(id=aid).first()

    user.concern.remove(aid)
    activity.concern.remove(user.id)

    user.save()
    activity.save()

def getComments(comments):
	result = []
	for comment in comments:
		usr = User.objects(id=comment.user_id).first()
		result.append((usr.username, comment.content, usr.avatar, comment.date))
	return result

def saveComment(email, aid, date_, content_):
	user = findUserByEmail(email)
	activity = Activity.objects(id=aid).first()
	activity.comments.append(Comment(content=content_, user_id=str(user.id), date=date_))
	activity.save()

