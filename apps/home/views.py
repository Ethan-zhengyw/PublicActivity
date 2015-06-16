# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def explore(request):
    activities = md.findAllActivities()[:8]
    # tmp = get_template('home.html')
    # html = tmp.render(Context({'activities' : activities}))
    # return HttpResponse(html)

    return render(request, 'home.html', {'activities': activities, "user": request.session['username']})


def host(request):

    # activities = md.findConcernedActivities(request.session['email'])
    user = md.findCurrentUser('123@123.com')
    acts_con, acts_par, acts_cre = md.findConcernedActivities('123@123.com')
    return render(request, 'host.html', {
        'acts_con': acts_con,
        'acts_par': acts_par,
        'acts_cre': acts_cre,
        'user': user
    })
