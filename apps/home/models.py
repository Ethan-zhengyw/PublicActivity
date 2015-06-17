# -*- coding: utf-8 -*-
from model.user import *
from model.activity import *
def findAllActivities():
    result = Activity.objects.all()
    return result

def findConcernedActivities(email):
    # user = User(
    #     username='Ethan',
    #     password=md5HashPwd('123'),
    #     email='123@123.com',
    #     user_type=0,
    #     introduction='123123123',
    #     avatar='/img/user.png',
    #     gender=1,
    #     tags='敬老,植树',
    #     
    #     concern = [
    #         "557e33898cc72815585952b4",
    #         "557e33898cc72815585952b5",
    #         "557e33898cc72815585952b6",
    #         "557e33898cc72815585952b7",
    #         "557e33898cc72815585952b8",
    #         "557e33898cc72815585952b9"
    #     ],

    #     participate = [
    #         "557e33898cc72815585952b4",
    #         "557e33898cc72815585952b9"
    #     ],

    #     create = [
    #         "557e33898cc72815585952b4",
    #         "557e33898cc72815585952b9"
    #     ]
    # )

    # print user
    # user.save()
    # print '1111'
    
    user = User.objects(email=email).first()
    result_con = []
    result_par = []
    result_cre = []
    for idx in user.concern:
        result_con.append(Activity.objects(id=idx).first())
    for idx in user.participate:
        result_par.append(Activity.objects(id=idx).first())
    for idx in user.create:
        result_cre.append(Activity.objects(id=idx).first())

    return result_con, result_par, result_cre

def findCurrentUser(email):
    user = User.objects(email=email).first()
    return user
