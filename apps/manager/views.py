# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import models as md

def manager(request):
    activities = md.findNotPassedActivities()
    return render(request, 'manager.html', {'activities': activities})

def setPass(request, aid):
    md.setPass(aid)
    print '通过'
    return HttpResponseRedirect("/manager")


def setFailPass(request, aid):
    md.setFailPass(aid)
    print '不通过'
    return HttpResponseRedirect("/manager")
