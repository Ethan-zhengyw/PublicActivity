from model.user import *

def addUser(email, password, usertype):
	p = User(email=email, password=md5HashPwd(password), user_type=usertype, username=email)
	p.save()

def checkEmail(email):
	user = User.objects(email=email).first()
	if not user:
		return True
	else:
		return False