from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def signin(request):
	return render(request, 'signin.html', {'user': 'Ethan'})

def s_signin(request):
	if 'email' in request.POST and 'password' in request.POST:
		email = request.POST['email']
		password = request.POST['password']
		user = md.check(email, password)
		if user:
			request.session['email'] = email
			request.session['user_type'] = user.user_type
			return HttpResponse("{'status': '1'}")
		else:
			return HttpResponse("{'status': '0', 'message' : 'Login Error'}")
	return HttpResponse("{}")

def logout(request):
	del request.session['email']
	del request.session['user_type']
	return HttpResponse("{}")	