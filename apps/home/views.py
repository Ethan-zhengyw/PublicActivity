# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import models as md
import datetime

def explore(request):

    activities = md.findAllActivities()
    acts_now = [act for act in activities if (act.deadline - datetime.datetime.now()).total_seconds() > 0]
    acts_off = [act for act in activities if (act.deadline - datetime.datetime.now()).total_seconds() < 0]

    if 'username' in request.session:
        username = request.session['username']
        avatar = request.session['avatar']
        user_type = md.findCurrentUser(request.session['email']).user_type
    else:
        username = None
        avatar = None
        user_type = None

    return render(request, 'home.html', {
        'activities': activities,
        'acts_now': acts_now,
        'acts_off': acts_off,
        "user": username,
        "avatar": avatar,
        'user_type': user_type
    })


def host(request):
    if 'username' in request.session:
        username = request.session['username']
        avatar = request.session['avatar']
        email = request.session['email']
    else:
        username = None
        avatar = None
        return HttpResponseRedirect('/home')

    acts_con, acts_par, acts_cre = md.findConcernedActivities(request.session['email'])
    return render(request, 'host.html', {
        'acts_con': acts_con,
        'acts_par': acts_par,
        'acts_cre': acts_cre,
        "avatar": avatar,
        'email': email,
        'user': username,
    })
