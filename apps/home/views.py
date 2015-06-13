# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import models as md

def explore(request):
	activities = md.findAllActivities()
    tmp = get_template('home.html')
    html = tmp.render(Context({'activities' : activities}))
    return HttpResponse(html)


def host(request):
	activities = md.findConcernedActivities(request.session['email'])
    tmp = get_template('host.html')
    html = tmp.render(Context({'activities' : activities}))
    return HttpResponse(html)