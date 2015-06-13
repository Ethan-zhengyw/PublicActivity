from django.db import models
def findAllActivities():
	result = Activity.objects.all()
	return result

def findConcernedActivities(email):
	user = User.objects(email=email).first()
	result_con = []
	result_par = []
	result_cre = []
	for idx in user.concern:
		result_con.append(Activity.objects(id=idx).first()
	for idx in user.participate:
		result_par.append(Activity.objects(id=idx).first()
	for idx in user.create:
		result_cre.append(Activity.objects(id=idx).first()
	return (result_con, result_par, result_cre)
# Create your models here.
