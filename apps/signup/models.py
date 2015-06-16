from model.user import *

def addUser(email, password, gender, username, tags):
	defaultAvatar = "/img/default_avatar.png"
	p = User(email=email, password=md5HashPwd(password),
			username=username, tags=tags,
			gender=gender, avatar=defaultAvatar)
	p.save()

def checkEmail(email):
	user = User.objects(email=email).first()
	if not user:
		return True
	else:
		return False