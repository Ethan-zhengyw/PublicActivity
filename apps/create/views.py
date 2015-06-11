# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import datetime
import models as md

def create(request):
    return render(request, 'create.html', {'user': 'Ethan'})

def s_create(request):
    print 'creating activity'

    name = request.POST['name']
    location = request.POST['location']
    introduction = request.POST['introduction']
    host = request.POST['host']
    create_time = datetime.datetime.now()
    # start_time = request.POST['starttime']
    # deadline = request.POST['deadline']
    start_time = datetime.datetime.now()
    deadline = datetime.datetime.now()
    creater_id = str(md.findUser(request.session['email']).id)

    print request
    print name, location, host, create_time, start_time, deadline, creater_id
    print datetime.datetime.now()

    tagsDict = {'tag_teach': '支教', 'tag_blood': '献血', 'tag_pe': '体育', 'tag_music': '音乐', 'tag_tree': '环保', 'tag_old': '敬老'}
    tags = [tagsDict[key] for key in tagsDict if key in request.POST]
    print tags

    md.addActivity(name, location, introduction, host, create_time, start_time, deadline, creater_id, tags)
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

