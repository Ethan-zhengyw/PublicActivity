# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def explore(request):
    activities = md.findAllActivities()[:8]
    # tmp = get_template('home.html')
    # html = tmp.render(Context({'activities' : activities}))
    # return HttpResponse(html)
    if 'username' in request.session:
        username = request.session['username']
        avatar = request.session['avatar']
    else:
        username = None
        avatar = None
    return render(request, 'home.html', {'activities': activities, "user": username, "avatar": avatar})


def host(request):
    if 'username' in request.session:
        username = request.session['username']
        avatar = request.session['avatar']
        email = request.session['email']
    else:
        username = None
        avatar = None
        return HttpResponseRedirect('/home')
    # user = md.findCurrentUser(request.session['email'])
    acts_con, acts_par, acts_cre = md.findConcernedActivities(request.session['email'])
    return render(request, 'host.html', {
        'acts_con': acts_con,
        'acts_par': acts_par,
        'acts_cre': acts_cre,
        "avatar": avatar,
        'email': email,
        'user': username,
    })
