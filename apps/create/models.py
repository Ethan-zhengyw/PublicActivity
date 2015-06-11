from model.user import *
from model.activity import *

def findUser(email):
    return User.objects(email=email).first()


def addActivity(name, location, introduction,
        host, create_time, start_time,
        deadline, creater_id, tags):
    activity = Activity(name=name, location=location,
            introduction=introduction, host=host, create_time=create_time,
            start_time=start_time, deadline=deadline, creater_id=creater_id, tags=tags)
    activity.save()
    print activity
