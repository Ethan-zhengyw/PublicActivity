from model.user import *

def checkEmail(email):
    user = User.objects(email=email).first()
    if not user:
        return True
    else:
        return False

def updatePwd(e_mail, oldPwd, newPwd, confirmPwd):
    print '/setting/models/updatePwd'

    # check original password and the username match or not
    user = User.objects(email=e_mail,
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
def updateBasicInfo(e_mail, introduction, gender, avatar, tags):
    print '/setting/models/updateBasicInfo'

    user = User.objects(email=e_mail).first()
    if user:
        user.introduction = introduction
        user.gender = gender
        user.avatar = avatar
        user.tags = tags
        user.save()
        print 'user basic info updated!'

def findUser(email):
    user = User.objects(email=email).first()
    print user.username
    print user.email
    return user
