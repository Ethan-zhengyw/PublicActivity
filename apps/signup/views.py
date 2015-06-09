from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def validEmail(email):
	return True

def validPassword(password):
	return True

def signup(request):
	return render(request, 'signup.html', {'user': 'Ethan'})

def s_signup(request):
	if 'email' in request.POST and 'password' in request.POST and "user_type" in request.POST:
		email = request.POST['email']
		password = request.POST['password']
		user_type = request.POST['user_type']
		if user_type == "1" or user_type == "0":
			if validEmail(email) and validPassword(password):
				if md.checkEmail(email):
					md.addUser(email, password, user_type)
					return HttpResponse("{'status': '1'}")
				else:
					return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")
	return HttpResponse("{}")

