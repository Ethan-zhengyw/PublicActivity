from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import models as md

def setting(request):
    #TODO check whether user have signin
    print request.session['email']
    return render(request, 'setting.html', {'user': md.findUser('123@123.com')})


def s_setting(request):

    oldPwd = request.POST['oldPwd']
    newPwd = request.POST['newPwd']
    confirmPwd = request.POST['confirmPwd']

    print request.POST['gender']

    md.updatePwd('Amanda', oldPwd, newPwd, confirmPwd)

    introduction = request.POST['introduction']
    gender = request.POST['gender']
    md.updateBasicInfo(introduction, gender)

    return HttpResponseRedirect('/setting')
