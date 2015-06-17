# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import models as md

def manager(request):

    if 'email' not in request.session:
        return HttpResponse('必须登录才可以进行活动审批')

    else:

        user = md.findUser(request.session['email'])

        if user.user_type != 0:
            return HttpResponse('必须是管理员才可以进行活动的审批')

        else:
            activities = md.findNotPassedActivities()
            return render(request, 'manager.html', {
                'activities': activities,
                'user': user.username,
                'avatar': user.avatar,
                'user_type': user.user_type
            })

def setPass(request, aid):
    md.setPass(aid)
    print '通过'
    return HttpResponseRedirect("/manager")


def setFailPass(request, aid):
    md.setFailPass(aid)
    print '不通过'
    return HttpResponseRedirect("/manager")
