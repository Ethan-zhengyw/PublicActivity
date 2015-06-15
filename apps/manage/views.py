# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import models as md

def manage(request):
	activities = md.findNotPassedActivities()
    return render(request, 'manage.html', {'activities': activities})

def setPass(request, aid):
	md.setPass(aid)
	return HttpResponseRedirect("/manage")