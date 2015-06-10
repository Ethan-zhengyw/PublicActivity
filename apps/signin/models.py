from model.user import *

def check(email, password):
	user = User.objects(email=email, password=md5HashPwd(password)).first()
	print md5HashPwd(password)
	return user
