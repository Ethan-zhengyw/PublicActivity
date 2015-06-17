# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import datetime
import models as md
import os

def create(request):

    if 'email' not in request.session:
        return HttpResponse("需要登录后才能发布活动")

    user = md.findUser(request.session['email'])

    return render(request, 'create.html', {
        'user': user.username,
        'avatar': user.avatar,
        'user_type': user.user_type
    })

def s_create(request):

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
    postImg = request.FILES['post']


    md.addActivity(name, location, introduction, host, create_time, start_time, deadline, creater_id, tags, postImg, request.session['email'])

    return HttpResponseRedirect('/home')

