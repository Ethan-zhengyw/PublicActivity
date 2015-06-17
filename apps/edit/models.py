from model.user import *
from model.activity import *
import datetime

def findUser(email):
    return User.objects(email=email).first()

def findActById(aid):
    return Activity.objects(id=aid).first()


def updateActivity(
    name, location, introduction,
    host, create_time, start_time,
    deadline, tags, postImg, aid):

    activity = findActById(aid)

    activity.name=name
    activity.location=location
    activity.introduction=introduction
    activity.host=host

    # TODO
    activity.start_time=getDatetimeFromStr(start_time)
    activity.deadline=getDatetimeFromStr(deadline)

    activity.tags=tags

    if postImg:
        activity.post = '/img/post/' + str(activity.id) + '_' + postImg.name
        f = open('./static/img/post/' + str(activity.id) + '_' + postImg.name, 'w')
        f.write(postImg.read())
        f.close()

    activity.save()


def getDatetimeFromStr(datetime_str):
    
   return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
