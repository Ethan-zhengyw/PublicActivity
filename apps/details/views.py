from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

import datetime
import models as md

class Comment:
    def __init__(self, user_name, content, avatar, date):
        self.user_name = user_name
        self.content = content
        self.avatar = avatar
        self.date = date

def details(request, aid):
    
    print aid
    activity = md.findActivityById(aid)
    number1 = len(activity.participate)
    number2 = len(activity.concern)

    tags = activity.tags.split(',')
    temp_result = md.getComments(activity.comments)
    comments = []
    for item in temp_result:
        comments.append(Comment(item[0], item[1], item[2], item[3]))

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
            'user_type': user.user_type,
            'isPar': isPar,
            'isCon': isCon,
            'comments' : comments
        })

    else:

        return render(request, 'details.html', {
            'activity': activity,
            'number1': number1,
            'number2': number2,
            'tags': tags,
            'user': None,
            'avatar': None,
            'comments' : comments
        })

def makeComment(request, aid):
    email = request.session['email']
    content = request.POST['content']
    date = datetime.datetime.now()
    md.saveComment(email, aid, date, content)
    return HttpResponseRedirect('/details/' + aid)

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
