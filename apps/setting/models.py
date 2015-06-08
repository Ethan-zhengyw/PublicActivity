from model.user import *

def updatePwd(username, oldPwd, newPwd, confirmPwd):
    print '/setting/models/updatePwd'

    # check original password and the username match or not
    user = User.objects(username=username,
            password=md5HashPwd(oldPwd)).first()

    if not user:
        print 'input wrong original password!'
    elif newPwd != confirmPwd:
        print 'two input of new password doesn\'t match!'
    else:
        # can update password now
        user.password = md5HashPwd(newPwd)
        user.save()
        print 'user password updated!'


# only update the gender and introduction
def updateBasicInfo(introduction, gender):
    print '/setting/models/updateBasicInfo'

    user = User.objects(username='Amanda').first()
    if user:
        user.introduction = introduction
        user.gender = gender
        user.save()
        print 'user basic info updated!'
