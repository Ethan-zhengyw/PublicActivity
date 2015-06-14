from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

import models as md

def details(request, aid):
    
    print aid
    activity = md.findActivityById(aid)
    number1 = len(activity.participate)
    number2 = len(activity.concern)

    tags = activity.tags.split(',')

    return render(request, 'details.html', {
        'activity': activity,
        'number1': number1,
        'number2': number2,
        'tags': tags
    })


def s_setting(request):

    oldPwd = request.POST['oldPwd']
    newPwd = request.POST['newPwd']
    confirmPwd = request.POST['confirmPwd']

    print request.POST['gender']

    md.updatePwd(request.session['email'], oldPwd, newPwd, confirmPwd)

    introduction = request.POST['introduction']
    gender = request.POST['gender']
    avatar = request.POST['avatar']
    tags = request.POST['tags']
    md.updateBasicInfo(introduction, gender, avatar, tags)

    return HttpResponseRedirect('/setting')
