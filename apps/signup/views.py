from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import re
import models as md

def validEmail(email):
    emailPattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
    match = emailPattern.findall(email)
    if match:
        return True
    return False

def validPassword(password):
    pattern = re.compile(r'([a-z0-9A-Z])+')
    match = pattern.findall(password)
    if match:
        return True
    return False

def signup(request):
    return render(request, 'signup.html', {'user': 'Ethan'})

def checkUsedEmail(request):
    if 'email' in request.POST:
        email = request.POST['email']
        if md.checkEmail(email):
            return HttpResponse("{'status': '1'}")
        else:
            return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")
    return HttpResponse("{}")

def s_signup(request):
    if 'email' in request.POST and 'username' in request.POST and 'password' in request.POST and 'tags' in request.POST and 'gender' in request.POST:
        gender = int(request.POST['gender'])
        tags = request.POST['tags']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if validEmail(email) and validPassword(password):
            if md.checkEmail(email):
                md.addUser(email, password, gender, username, tags)
                return HttpResponse("{'status': '1'}")
            else:
                return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")
        else:
            if not validEmail(email):
                print "email"
            if not validPassword(password):
                print "password"
    return HttpResponse("{}")

