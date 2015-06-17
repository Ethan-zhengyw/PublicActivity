# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import datetime
import models as md
import os

def edit(request, aid):

    if 'email' not in request.session:
        return HttpResponse("需要登录后才能编辑活动")

    user = md.findUser(request.session['email'])
    activity = md.findActById(aid)

    return render(request, 'edit.html', {
        'activity': activity,
        'user': user.username,
        'avatar': user.avatar
    })

def s_edit(request, aid):

    print 'creating activity'

    name = request.POST['name']
    location = request.POST['location']
    introduction = request.POST['introduction']
    host = request.POST['host']
    create_time = datetime.datetime.now()
    start_time = request.POST['start_time']
    deadline = request.POST['deadline']
    tags = request.POST['tags']

    if 'post' in request.FILES:
        postImg = request.FILES['post']
    else:
        postImg = None

    md.updateActivity(name, location, introduction, host, create_time, start_time, deadline, tags, postImg, aid)

    return HttpResponseRedirect('/details/' + aid)
