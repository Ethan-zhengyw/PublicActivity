from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

import models as md

def details(request, aid):
    
    print aid
    activity = md.findActivityById(aid)
    number1 = len(activity.participate)
    number2 = len(activity.concern)

    tags = activity.tags.split(',')

    if 'email' in request.session:
        user = md.findUserByEmail(request.session['email'])

        isPar = md.checkPar(request.session['email'], aid)
        isCon = md.checkCon(request.session['email'], aid)

        return render(request, 'details.html', {
            'activity': activity,
            'number1': number1,
            'number2': number2,
            'tags': tags,
            'user': user.username,
            'avatar': user.avatar,
            'isPar': isPar,
            'isCon': isCon
        })

    else:

        return render(request, 'details.html', {
            'activity': activity,
            'number1': number1,
            'number2': number2,
            'tags': tags,
            'user': None,
            'avatar': None
        })


def setPar(request, aid):
    
    email = request.session['email']
    md.setPar(email, aid)
    
    return HttpResponseRedirect('/details/' + aid)

def setCon(request, aid):
    
    email = request.session['email']
    md.setCon(email, aid)

    return HttpResponseRedirect('/details/' + aid)

def unsetPar(request, aid):
    
    email = request.session['email']
    md.unsetPar(email, aid)
    
    return HttpResponseRedirect('/details/' + aid)

def unsetCon(request, aid):
    
    email = request.session['email']
    md.unsetCon(email, aid)

    return HttpResponseRedirect('/details/' + aid)
