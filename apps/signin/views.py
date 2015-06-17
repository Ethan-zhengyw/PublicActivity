from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def signin(request):
        if 'email' in request.session:
            return HttpResponseRedirect('/home')


	if 'username' in request.session:
		username = request.session['username']
	else:
		username = None
	return render(request, 'signin.html', {
            'user': username,
            'avatar': None,
            'user_type': None
        })

def s_signin(request):
	if 'email' in request.POST and 'password' in request.POST:
		email = request.POST['email']
		password = request.POST['password']
		user = md.check(email, password)
		if user:
			request.session['email'] = email
			request.session['username'] = user.username
			request.session['avatar'] = user.avatar
			return HttpResponse("{'status': '1', 'message' : 'Login succeed'}")
		else:
			return HttpResponse("{'status': '0', 'message' : 'Login Error'}")

def logout(request):
        if 'email' in request.session:
            del request.session['email']
            del request.session['username']
            del request.session['avatar']
	return HttpResponseRedirect('/home')
