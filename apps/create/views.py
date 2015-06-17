# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import datetime
import models as md

def create(request):
    return render(request, 'create.html', {'user': 'Ethan'})

def s_create(request):

    if 'email' not in request.session:
        return HttpResponse("需要登录后才能发布活动")


    print request.POST
    print 'creating activity'


    name = request.POST['name']
    location = request.POST['location']
    introduction = request.POST['introduction']
    host = request.POST['host']
    create_time = datetime.datetime.now()
    start_time = request.POST['start_time']
    deadline = request.POST['deadline']
    creater_id = str(md.findUser(request.session['email']).id)
    tags = request.POST['tags']
    # post = request.POST['post']

    print name, location, host, create_time, start_time, deadline, creater_id, tags
    print request
    print '--------------------------'
    print request.FILES

    # md.addActivity(name, location, introduction, host, create_time, start_time, deadline, creater_id, tags)
    # if 'email' in request.POST and 'password' in request.POST and 'confirmPwd' in request.POST and "user_type" in request.POST:
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     confirmPwd = request.POST['confirmPwd']
    #     user_type = request.POST['user_type']
    #     if user_type == "1" or user_type == "0":
    #         if validEmail(email) and validPassword(password):
    #             if password == confirmPwd:
    #                 if md.checkEmail(email):
    #                     md.addUser(email, password, user_type)
    #                     return HttpResponse("{'status': '1'}")
    #                 else:
    #                     return HttpResponse("{'status': '0', 'message' : 'Email already in use'}")
    #             else:
    #                 return HttpResponse("{'status': '0', 'message' : 'two input password doesn't match'}")

    return HttpResponse("{}")

