from model.user import *
from model.activity import *
import datetime

def findUser(email):
    return User.objects(email=email).first()


def addActivity(
    name, location, introduction,
    host, create_time, start_time,
    deadline, creater_id, tags, postImg, email):

    activity = Activity(
        isPass=0,
        name=name,
        location=location,
        introduction=introduction,
        host=host,
        create_time=create_time,
        start_time=getDatetimeFromStr(start_time),
        deadline=getDatetimeFromStr(deadline), 
        creater_id=creater_id,
        tags=tags)

    # save activity to generate id
    activity.save()

    activity.post = '/img/post/' + str(activity.id) + '_' + postImg.name
    activity.save()

    f = open('./static/img/post/' + str(activity.id) + '_' + postImg.name, 'w')
    f.write(postImg.read())
    f.close()

    # update user's create list
    user = findUser(email)
    user.create.append(activity.id)
    user.save()

    print activity


def getDatetimeFromStr(datetime_str):
    
   return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
