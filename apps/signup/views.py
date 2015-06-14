from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import re
import models as md

def validEmail(email):
    emailPattern = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
    match = pattern.findall(password)
    if match:
        return True
    return False

def validPassword(password):
    pattern = re.compile(r'([^a-z0-9A-Z])+')
    match = pattern.findall(password)
    if match:
        return len(password) > 8
    return False

def signup(request):
    return render(request, 'signup.html', {'user': 'Ethan'})

def checkUsedEmail(request):
    if 'email' in request.POST:
        if md.checkEmail(email):
            md.addUser(email, password, user_type)
            return HttpResponse("{'status': '1'}")
        else:
            return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")
    return HttpResponse("{}")

def s_signup(request):
    if 'email' in request.POST and 'username' in request.POST and 'password' in request.POST and 'tags' in request.POST and 'gender' in request.POST  and "user_type" in request.POST:
        gender = request.POST['gender']
        tags = request.POST['tags']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']
        if user_type == "1" or user_type == "0":
            if validEmail(email) and validPassword(password):
                if md.checkEmail(email):
                    md.addUser(email, password, user_type, gender, username, tags)
                    return HttpResponse("{'status': '1'}")
                else:
                    return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")

    return HttpResponse("{}")

